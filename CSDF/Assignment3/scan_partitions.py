import struct
import os
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='forensic_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info("Starting scan_partitions.py")

# Partition type lookup table
PARTITION_TYPES = {
    0x07: "NTFS",
    0x0B: "FAT32",
    0x0C: "FAT32 (LBA)",
    0x83: "ext2/ext3",
    0x00: "Empty",
    # Add more as needed; non-standard types (e.g., 0x72) will show as "Unknown"
}

def parse_mbr(f):
    f.seek(0)
    mbr = f.read(512)
    if mbr[510:512] != b"\x55\xAA":
        print("[*] No valid MBR signature (0x55AA) detected.")
        logging.info("No valid MBR signature detected")
        return
    print("[*] MBR signature found.")
    logging.info("MBR signature found")
    image_sectors = os.path.getsize(f.name) // 512
    print(f"[*] Image size: {os.path.getsize(f.name)} bytes, sectors: {image_sectors}")
    logging.info(f"Image size: {os.path.getsize(f.name)} bytes, sectors: {image_sectors}")
    print("[*] MBR partition entries:")
    for i in range(4):
        entry = mbr[446 + i*16:446 + (i+1)*16]
        status = entry[0]
        type_code = entry[4]
        start_lba = int.from_bytes(entry[8:12], "little")
        sectors = int.from_bytes(entry[12:16], "little")
        type_name = PARTITION_TYPES.get(type_code, f"Unknown (0x{type_code:02x})")
        if type_code != 0:
            print(f"  Partition {i+1}: type={type_name} start_lba={start_lba} sectors={sectors} status=0x{status:02x}")
            logging.info(f"Partition {i+1}: type={type_name} start_lba={start_lba} sectors={sectors} status=0x{status:02x}")
            if start_lba + sectors > image_sectors:
                print(f"[!] Warning: Partition {i+1} exceeds image size (start_lba + sectors = {start_lba + sectors} > {image_sectors})")
                logging.warning(f"Partition {i+1} exceeds image size (start_lba + sectors = {start_lba + sectors} > {image_sectors})")

def scan_for_filesystem_signatures(f, max_sectors=200000):
    candidates = []
    image_sectors = min(os.path.getsize(f.name) // 512, max_sectors)
    f.seek(0)
    for sector in range(image_sectors):
        f.seek(sector * 512)
        buf = f.read(512)
        if buf[3:11] == b"NTFS    ":
            candidates.append((sector, "NTFS"))
        elif buf[0:8] == b"\xEB\x52\x90FAT32   ":
            candidates.append((sector, "FAT32"))
    if candidates:
        print("[+] Found candidate filesystem starts (sector, fs):")
        for sector, fs in candidates:
            print(f"  Sector {sector} (LBA {sector}) -> {fs}")
            logging.info(f"Found filesystem: Sector {sector} -> {fs}")
    else:
        print("[-] No common filesystem signatures found.")
        logging.info("No filesystem signatures found")
    return candidates

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} image.dd")
        logging.error("Invalid arguments")
        sys.exit(1)
    img = sys.argv[1]
    with open(img, "rb") as f:
        parse_mbr(f)
        candidates = scan_for_filesystem_signatures(f)
    print("Tip: Common partition starts: 2048, 4096, etc. Use these LBAs to reconstruct partition table with tools like testdisk/fdisk (read docs).")
    logging.info("Completed scan_partitions.py")
