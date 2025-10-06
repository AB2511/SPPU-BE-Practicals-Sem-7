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
  * `image.dd` (sample disk image)
* **Description:**

  * `recover_files.py`: Simple file carver that recovers deleted JPG, PNG, PDF files from raw disk images.
  * `scan_partitions.py`: Scans disk images for common partition signatures (MBR, NTFS, FAT32, exFAT).
* **Output:**

  * Shows recovered files in the output folder.
  * Prints candidate partitions and sector locations.

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

* `image.dd` can be created manually using `fsutil` (Windows) or `dd` (Linux),
  or downloaded from **Digital Corpora (NPS Test Disk Images)** for realistic forensic testing.

### 💾 How to Create `.dd` File

#### 🔹 On Windows:

You can use the `fsutil` command to create a dummy disk image file:

```bash
fsutil file createnew image.dd 104857600
```

This command creates a 100 MB (`104857600` bytes) blank disk image named `image.dd` in the current directory.

You can change the size as per your need (e.g., `52428800` for 50 MB).

> ⚠️ Note: `fsutil` requires Administrator privileges.

#### 🔹 On Linux:

You can use the `dd` command:

```bash
dd if=/dev/zero of=image.dd bs=1M count=100
```

This creates a 100 MB blank disk image.

---

* These programs are for **educational purposes only** (SPPU LP4 practicals).
* Do not use on live systems without permission.

---

✍️ Prepared for **SPPU BE Computer Engineering – Cyber Security & Digital Forensics Lab (LP4)**
