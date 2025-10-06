import os
import io
import csv
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='forensic_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info("Starting recover_files.py")

def find_all_offsets(data, signature):
    offsets = []
    start = 0
    while True:
        start = data.find(signature, start)
        if start == -1:
            break
        offsets.append(start)
        start += 1
    return offsets

def validate_jpeg(data):
    # Check for JPEG markers in first 512 bytes (more permissive)
    valid_markers = [b"\xff\xc0", b"\xff\xc2", b"\xff\xc4", b"\xff\xda", b"\xff\xdb"]
    for marker in valid_markers:
        if marker in data[:512]:
            return True
    return False

def recover_from_image(img_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    
    valid_count = 0
    invalid_count = 0
    report_data = []
    
    with open(img_path, "rb") as f:
        data = f.read()
    
    # JPEG carving
    for start in find_all_offsets(data, b"\xff\xd8"):
        end = data.find(b"\xff\xd9", start + 2)
        if end == -1 or end - start > 10_000_000:  # Cap file size
            continue
        jpg_data = data[start:end + 2]
        filename = f"recovered_{valid_count + invalid_count:04d}.jpg"
        is_valid = validate_jpeg(jpg_data)
        validity = "Valid" if is_valid else "Invalid"
        out_path = os.path.join(out_dir, filename)
        
        with open(out_path, "wb") as out:
            out.write(jpg_data)
        print(f"Recovered {filename} at offset {start} ({validity})")
        logging.info(f"Recovered {filename} at offset {start} ({validity})")
        
        # Add to report
        report_data.append({
            "filename": filename,
            "offset": start,
            "size": end - start + 2,
            "filetype": "JPG",
            "validity": validity
        })
        
        if is_valid:
            valid_count += 1
        else:
            invalid_count += 1
    
    # Write CSV report
    csv_path = os.path.join(out_dir, "recovery_report.csv")
    with open(csv_path, "w", newline="") as csvfile:
        fieldnames = ["filename", "offset", "size", "filetype", "validity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in report_data:
            writer.writerow(row)
    logging.info(f"Generated recovery_report.csv at {csv_path}")
    
    print(f"[+] Finished. Recovered {valid_count + invalid_count} files to '{out_dir}'")
    print(f"  Valid files: {valid_count}")
    print(f"  Invalid files: {invalid_count}")
    logging.info(f"Recovered {valid_count} valid, {invalid_count} invalid files")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} image.dd output_folder")
        logging.error("Invalid arguments")
        sys.exit(1)
    img_path = sys.argv[1]
    out_dir = sys.argv[2]
    recover_from_image(img_path, out_dir)
    logging.info("Completed recover_files.py")
