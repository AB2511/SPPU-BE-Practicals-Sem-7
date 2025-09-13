"""
Simple file-carving demo (JPEG, PNG, PDF).
Usage:
    python recover_files.py image.dd output_folder
Notes:
- Works best on disk image files (raw dd images). Avoid running on live disks.
- This is a teaching/demo tool. It is not a full forensic suite.
"""

import os
import sys

SIGNATURES = {
    "jpg": {
        "start": b"\xff\xd8",
        "end": b"\xff\xd9",
    },
    "png": {
        "start": b"\x89PNG\r\n\x1a\n",
        # We'll search for the IEND chunk and include its 12-byte trailer
        "end_marker": b"IEND",
        "end_trailer_len": 12,
    },
    "pdf": {
        "start": b"%PDF",
        "end": b"%%EOF",
    }
}

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def find_all_offsets(data, pattern):
    """Return list of offsets where pattern occurs."""
    offs = []
    i = data.find(pattern)
    while i != -1:
        offs.append(i)
        i = data.find(pattern, i+1)
    return offs

def recover_from_image(img_path, out_dir):
    with open(img_path, "rb") as f:
        data = f.read()

    ensure_dir(out_dir)
    recovered_count = 0

    # JPEG
    for start in find_all_offsets(data, SIGNATURES["jpg"]["start"]):
        # find nearest end after start
        end = data.find(SIGNATURES["jpg"]["end"], start+2)
        if end != -1:
            end += len(SIGNATURES["jpg"]["end"])
            fname = os.path.join(out_dir, f"recovered_{recovered_count:04d}.jpg")
            with open(fname, "wb") as out:
                out.write(data[start:end])
            recovered_count += 1

    # PNG
    for start in find_all_offsets(data, SIGNATURES["png"]["start"]):
        # find the IEND chunk after start
        iend = data.find(SIGNATURES["png"]["end_marker"], start+8)
        if iend != -1:
            # include 12 bytes trailer after IEND marker (length+IEND+CRC)
            end = iend + SIGNATURES["png"]["end_trailer_len"]
            fname = os.path.join(out_dir, f"recovered_{recovered_count:04d}.png")
            with open(fname, "wb") as out:
                out.write(data[start:end])
            recovered_count += 1

    # PDF
    for start in find_all_offsets(data, SIGNATURES["pdf"]["start"]):
        # find the EOF marker after start
        eof = data.find(SIGNATURES["pdf"]["end"], start+4)
        if eof != -1:
            eof += len(SIGNATURES["pdf"]["end"])
            # PDFs sometimes have garbage after EOF; include a small window
            end = eof + 4
            fname = os.path.join(out_dir, f"recovered_{recovered_count:04d}.pdf")
            with open(fname, "wb") as out:
                out.write(data[start:end])
            recovered_count += 1

    print(f"[+] Finished. Recovered {recovered_count} files to '{out_dir}'")
    if recovered_count == 0:
        print("[-] No matches found. Try on a larger / different image or add more signatures.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python recover_files.py image.dd output_folder")
        sys.exit(1)
    img_path = sys.argv[1]
    out_dir = sys.argv[2]
    recover_from_image(img_path, out_dir)
