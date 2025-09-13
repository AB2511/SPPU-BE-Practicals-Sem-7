"""
Scan a raw disk image to find possible partition start LBAs by looking for
boot-sector signatures (NTFS, FAT32). Read-only.
Usage:
    python scan_partitions.py image.dd
Notes:
- Sector size assumed 512 bytes. Modify if needed.
"""

import sys
import struct

SECTOR_SIZE = 512

def read_sector(f, sector_no):
    f.seek(sector_no * SECTOR_SIZE)
    return f.read(SECTOR_SIZE)

def parse_mbr(f):
    f.seek(0)
    mbr = f.read(SECTOR_SIZE)
    # Check MBR signature 0x55AA at offset 510
    sig = mbr[510:512]
    if sig == b'\x55\xaa':
        print("[*] MBR signature found.")
        # Partition entries start at offset 446, each 16 bytes
        parts = []
        for i in range(4):
            entry = mbr[446 + i*16 : 446 + (i+1)*16]
            status = entry[0]
            ptype = entry[4]
            lba_start = struct.unpack_from("<I", entry, 8)[0]
            num_sectors = struct.unpack_from("<I", entry, 12)[0]
            parts.append({
                "index": i+1,
                "status": status,
                "type": ptype,
                "lba_start": lba_start,
                "num_sectors": num_sectors
            })
        print("[*] MBR partition entries:")
        for p in parts:
            print(f"  Partition {p['index']}: type=0x{p['type']:02x} start_lba={p['lba_start']} sectors={p['num_sectors']} status=0x{p['status']:02x}")
    else:
        print("[*] No valid MBR signature (0x55AA) detected.")

def scan_for_filesystem_signatures(f, max_sectors=None):
    """
    Scan image sector-by-sector and look for common FS signatures:
      - NTFS: 'NTFS    ' at offset 3 of boot sector
      - FAT32: 'FAT32' in boot sector (offset ~82)
    Returns list of (sector_no, fs_type)
    """
    candidates = []
    f.seek(0, 2)
    size = f.tell()
    total_sectors = size // SECTOR_SIZE
    limit = total_sectors if max_sectors is None else min(total_sectors, max_sectors)
    print(f"[*] Image size: {size} bytes, sectors: {total_sectors}. Scanning up to {limit} sectors...")

    for s in range(0, limit):
        f.seek(s * SECTOR_SIZE)
        buf = f.read(SECTOR_SIZE)
        if len(buf) < SECTOR_SIZE:
            break

        # NTFS check: ASCII "NTFS    " at offset 3
        if buf[3:11] == b"NTFS    ":
            candidates.append((s, "NTFS"))
            # skip ahead a bit; partitions typically start at sector 2048 or similar
            # but don't skip too much in case there are multiple matches
        # FAT32 check: 'FAT32' appears near offset 82
        elif b"FAT32" in buf[82:90]:
            candidates.append((s, "FAT32"))
        # exFAT: signature 'EXFAT   ' at offset 3
        elif buf[3:11] == b"EXFAT   ":
            candidates.append((s, "exFAT"))
        # (You can add ext, HFS+, etc. by their respective superblock patterns)

    return candidates

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scan_partitions.py image.dd")
        sys.exit(1)
    img = sys.argv[1]
    with open(img, "rb") as f:
        parse_mbr(f)
        candidates = scan_for_filesystem_signatures(f, max_sectors=200000)  # limit optional
        if candidates:
            print("[+] Found candidate filesystem starts (sector, fs):")
            for sec, fs in candidates:
                print(f"  Sector {sec} (LBA {sec}) -> {fs}")
            print("\nTip: Common partition starts: 2048, 4096, etc. Use these LBAs to reconstruct partition table with tools like testdisk/fdisk (read docs).")
        else:
            print("[-] No common filesystem signatures found in scanned sectors.")
