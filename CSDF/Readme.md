# CSDF LP4 Practicals – BE Computer Engineering (SPPU)

This repository contains solutions for **CSDF (Cyber Security & Digital Forensics) Laboratory Practicals (LP4)** for **BE Computer Engineering (SPPU)**.
Each assignment includes code, sample input, and output demonstration.

---

## 📂 Assignment 1 – Email Forensics

**Title:** Write a program for Tracking Emails & Investigating Email Crimes (analyze e-mail header).

* **Files:**
  * `email_header_analyzer.py`
  * `header.txt` (sample email header)
* **Description:**
  Parses raw e-mail headers to extract and analyze fields such as:
  * `MIME-Version`, `Date`, `Subject`, `From`, `To`, `Delivered-To`
  * Multiple `Received` headers (to trace route of email)
* **Output:**
  Displays all required header fields, missing fields are flagged as `(not found)`.

---

## 📂 Assignment 2 – CAPTCHA Generation & Verification

**Title:** Implement a program to generate & verify CAPTCHA image.

* **Files:**
  * `textCaptcha.py` → Random alphanumeric CAPTCHA generation & verification
  * `imgCaptcha.py` → CAPTCHA image generation (`CAPTCHA.png`) using `captcha` library
* **Description:**
  * Generates CAPTCHA strings and verifies user input.
  * Creates CAPTCHA images with distorted text to prevent automated solving.
* **Output:**
  * Text-based CAPTCHA → shows "Matched / Not Matched".
  * Image-based CAPTCHA → saves `CAPTCHA.png`.

---

## 📂 Assignment 3 – File & Partition Recovery

**Title:** Write a computer forensic application program for Recovering Permanently Deleted Files and Deleted Partitions.

* **Files:**
  * `recover_files.py`
  * `scan_partitions.py`
  * `image.dd` (sample disk image, JPEG Search Test #1)
  * `recovered_files/recovery_report.csv` (recovery details)
  * `forensic_log.txt` (timestamped logs)

* **Description:**
  * `scan_partitions.py`: Scans raw disk images for partition signatures (MBR, NTFS, FAT32). Detects MBR signature (`0x55AA`), parses partition table, and identifies filesystem signatures (e.g., `NTFS`). Includes partition type lookup (e.g., `0x07` → NTFS), LBA validation warnings, and logging.
  * `recover_files.py`: Carves deleted JPG files from raw disk images using signatures (`\xff\xd8` to `\xff\xd9`). Validates JPGs with markers (`\xff\xc0`, `\xff\xc2`, `\xff\xc4`, `\xff\xda`, `\xff\xdb`), generates a CSV report, and logs actions with timestamps.

* **Output:**
  * **scan_partitions.py**:
    ```bash
    D:\BE Practicals\CSDF>python scan_partitions.py image.dd
    [*] MBR signature found.
    [*] Image size: 10289152 bytes, sectors: 20096
    [*] MBR partition entries:
      Partition 1: type=Unknown (0x72) start_lba=218129509 sectors=1701990410 status=0x63
    [!] Warning: Partition 1 exceeds image size (start_lba + sectors = 1920119919 > 20096)
      Partition 2: type=Unknown (0x74) start_lba=729050177 sectors=543974724 status=0x73
    [!] Warning: Partition 2 exceeds image size (start_lba + sectors = 1273024901 > 20096)
      Partition 3: type=Unknown (0x65) start_lba=168653938 sectors=0 status=0x74
    [!] Warning: Partition 3 exceeds image size (start_lba + sectors = 168653938 > 20096)
    [+] Found candidate filesystem starts (sector, fs):
      Sector 0 (LBA 0) -> NTFS
    Tip: Common partition starts: 2048, 4096, etc. Use these LBAs to reconstruct partition table with tools like testdisk/fdisk (read docs).
    ```
  * **recover_files.py**:
    ```bash
    D:\BE Practicals\CSDF>python recover_files.py image.dd recovered_files
    Recovered recovered_0000.jpg at offset 271360 (Valid)
    Recovered recovered_0001.jpg at offset 545792 (Valid)
    Recovered recovered_0002.jpg at offset 872960 (Valid)
    Recovered recovered_0013.jpg at offset 3424256 (Valid)
    Recovered recovered_0017.jpg at offset 5148672 (Valid)
    Recovered recovered_0028.jpg at offset 6166564 (Valid)
    Recovered recovered_0029.jpg at offset 6442825 (Valid)
    Recovered recovered_0030.jpg at offset 6594588 (Valid)
    [+] Finished. Recovered 31 files to 'recovered_files'
      Valid files: 8
      Invalid files: 23
    ```
  * **MD5 Verification**:
    ```bash
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0000.jpg MD5
    MD5 hash of recovered_0000.jpg: 75b8d00568815a36c3809b46fc84ba6d (matches file1.jpg - normal JPEG)
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0001.jpg MD5
    MD5 hash of recovered_0001.jpg: 0c452c5800fcfa7c66027ae89c4f068a (matches file7.hmm - deleted JPEG)
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0002.jpg MD5
    MD5 hash of recovered_0002.jpg: afd55222024a4e22f7f5a3a665320763 (matches file6.jpg - deleted JPEG)
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0013.jpg MD5
    MD5 hash of recovered_0013.jpg: 7fc3954d980a643e9eafd62e053cb075 (no match - likely partial JPEG)
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0017.jpg MD5
    MD5 hash of recovered_0017.jpg: de5d83153339931371719f4e5c924eba (matches file2.dat - JPEG with non-JPEG extension)
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0028.jpg MD5
    MD5 hash of recovered_0028.jpg: 35c9da622659465956cf2d210c89bf07 (no match - likely partial JPEG)
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0029.jpg MD5
    MD5 hash of recovered_0029.jpg: 936d202fbedecbe64b42c5f3d03233e5 (no match - likely partial JPEG)
    D:\BE Practicals\CSDF\recovered_files>certutil -hashfile recovered_0030.jpg MD5
    MD5 hash of recovered_0030.jpg: e8da0614474ae16081261e7c1222c337 (no match - likely partial JPEG)
    ```
  * **Additional Outputs**:
    - `recovery_report.csv`: Generated in `recovered_files/` with columns: filename, offset, size, filetype, validity.
    - `forensic_log.txt`: Timestamped logs (e.g., "2025-10-06 19:50:XX - Recovered recovered_0000.jpg at offset 271360 (Valid)").
    - Valid JPGs (`recovered_0000.jpg`, `recovered_0001.jpg`, `recovered_0002.jpg`, `recovered_0017.jpg`) display correctly in Windows Photos.

* **Results Analysis**:
  * **Partition Detection**: Successfully detected MBR (`0x55AA`) and NTFS signatures at sector 0. Non-standard partition types (e.g., `0x72`) and invalid LBAs (e.g., 218,129,509) were flagged as test artifacts with warnings, ensuring robust validation.
  * **File Recovery**: Recovered 31 files, with 8 valid JPGs (4 confirmed: `file1.jpg`, `file2.dat`, `file6.jpg` (deleted), `file7.hmm` (deleted) via MD5; 4 unmatched likely partial JPGs). Invalid files (23) from test cases like `file5.rtf` (multiple `0xffd8`). Offsets, sizes, and validity logged in `recovery_report.csv`.
  * **Improvements**: Added partition type lookup (e.g., `0x07` → NTFS), LBA validation warnings, JPEG validation (`\xff\xc0`, `\xff\xc4`, etc.), CSV reporting, and timestamped logging.
  * **Limitations**: Embedded files (e.g., `file8.jpg` in ZIP) and ADS (`file13.dll:here`) not recovered due to raw carving focus. NTFS at sector 0 may be a test artifact.

---

## 📂 Assignment 4 – Log Correlation

**Title:** Write a program for log correlation of multiple log files.

* **Files:**
  * `log_correlation.py`
  * `server1.log`
  * `server2.log`
* **Description:**
  * Reads two server log files.
  * Parses logs into structured format (timestamp, level, message).
  * Correlates warnings with the same message occurring within 10 seconds across logs.
* **Output:**
  Displays correlated warning events side by side.

---

## 🛠 Requirements

* Python 3.8+
* Libraries:
  * `captcha` (`pip install captcha`)
  * `Pillow` (installed automatically with `captcha`)

---

## 📌 How to Run

```bash
# Assignment 1
python email_header_analyzer.py
# Provide path to CSDF/Assignment1/header.txt when asked (or place header.txt in the same folder)

# Assignment 2
python textCaptcha.py
python imgCaptcha.py

# Assignment 3
python scan_partitions.py image.dd
python recover_files.py image.dd recovered_files

# Assignment 4
python log_correlation.py
```

---

## 📖 Notes

* The sample disk image (`image.dd`) for Assignment 3 is the JPEG Search Test #1 (8-jpeg-search.dd), a 10 MB NTFS raw disk image containing 10 JPG files (some deleted, embedded, or in ADS). Source: Digital Forensics Tool Testing (DFTT) project.

### 💾 How to Obtain `image.dd`

#### 🔹 Download from DFTT (Recommended):
The `image.dd` file was downloaded from the JPEG Search Test #1 ZIP, discovered via dfir.training and hosted on dftt.sourceforge.net/SourceForge. Follow these steps:

1. Visit [dfir.training Test Images](https://www.dfir.training/downloads/test-images?category[0]=11&category_children=1).
   - Lists forensic test images, including Digital Forensics Tool Testing Images.

2. Navigate to the DFTT home page: [dftt.sourceforge.net](https://dftt.sourceforge.net/).

3. Click "JPEG Search Test #1" under Test Images: [JPEG Search Test #1](https://dftt.sourceforge.net/test8/index.html).

4. In the "Download" section, click the ZIP link (`jpeg-search-test1.zip`, ~2 MB): [Direct ZIP Link](https://dftt.sourceforge.net/test8/jpeg-search-test1.zip).
   - Alternative: Browse the DFTT SourceForge project: [SourceForge DFTT](https://sourceforge.net/projects/dftt/), then locate `test8/jpeg-search-test1.zip`.

5. Extract the ZIP file to obtain `8-jpeg-search.dd` (10 MB NTFS raw image).
   - Rename to `image.dd` (optional, matches script usage).

6. Verify the MD5 hash to ensure integrity:
   ```bash
   certutil -hashfile image.dd MD5
   ```
   - Expected: `9bdb9c76b80e90d155806a1fc7846db5`

#### 🔹 Alternative Sources:
- **NIST CFReDS**: [cfreds.nist.gov](https://cfreds.nist.gov/projects/1/download/) (other forensic images).
- **Digital Corpora**: [downloads.digitalcorpora.org](https://downloads.digitalcorpora.org/corpora/drives/) (disk images, scenarios).

#### 🔹 Create a Dummy `.dd` File (Not Used):
For testing without downloading, create a blank disk image (not recommended for Assignment 3, as it lacks test files):

* **On Windows** (requires Administrator privileges):
  ```bash
  fsutil file createnew image.dd 104857600
  ```
  Creates a 100 MB blank disk image.

* **On Linux**:
  ```bash
  dd if=/dev/zero of=image.dd bs=1M count=100
  ```
  Creates a 100 MB blank disk image.

---

* These programs are for **educational purposes only** (SPPU LP4 practicals).
* Do not use on live systems without permission.
* Cite: "JPEG Search Test #1 from dftt.sourceforge.net."

---

✍️ Prepared for **SPPU BE Computer Engineering – Cyber Security & Digital Forensics Lab (LP4)**
