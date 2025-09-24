# SPPU BE Practicals Semester 7

This repository contains practical implementations for Semester 7 BE (Bachelor of Engineering) at Savitribai Phule Pune University (SPPU), covering **Machine Learning (ML)**, **Design and Analysis of Algorithms (DAA)**, **Cyber Security & Digital Forensics (CSDF)**, and **Software Testing & Quality Assurance (STQA)**.  
The assignments include Jupyter Notebooks, Python scripts, C++ files, Java programs, Excel files, and supporting datasets or documents. All code is for educational purposes only.

---

## Subjects and Assignments

### Machine Learning (ML)
1. **Uber Ride Price Prediction** (`MLAssignment1.ipynb`): Predict Uber ride prices using linear and random forest regression. Dataset: `uber.csv`.
2. **Bank Customer Churn Prediction** (`MLAssignment2.ipynb`): Build a neural network classifier. Dataset: `Churn_Modelling.csv`.
3. **Gradient Descent Algorithm** (`MLAssignment3.ipynb`): Find local minima of \( y = (x + 3)^2 \) with plotting.
4. **K-Nearest Neighbors on Diabetes** (`MLAssignment4.ipynb`): Implement KNN and compute metrics. Dataset: `diabetes.csv`.

---

### Design and Analysis of Algorithms (DAA)
1. **Fibonacci Numbers with Step Count**: Non-recursive (`Fibononrecur.cpp`) and Recursive (`Fiborecur.cpp`).
2. **Fractional Knapsack Problem** (`knapsack.py`): Solve using greedy method.
3. **0-1 Knapsack Problem** (`knapsack01.cpp`): Solve using dynamic programming.
4. **8-Queens Problem with Backtracking** (`nqueens.py`): Place queens on an 8x8 board.

---

### Cyber Security & Digital Forensics (CSDF – LP4)
1. **Tracking Emails & Investigating Email Crimes**: Parses raw email headers to trace suspicious emails.
2. **CAPTCHA Generation & Verification**: Generates random alphanumeric CAPTCHA strings and verifies user input.
3. **Recovering Permanently Deleted Files and Partitions**: Recovers deleted files from raw disk images using file carving; scans for partition signatures.
4. **Log Correlation**: Correlates multiple log files to detect events occurring close in time across systems.

---

### Software Testing & Quality Assurance (STQA – LP4)
1. **Gmail Login Testing** (`LoginTest.java`): Write Selenium automation scripts for Gmail login page; implement positive and negative scenarios.
2. **Excel Test Case Writing** (`CreateWriteExcelFile.java`): Generate Excel test case sheet for an application using Java and JExcelAPI or Maven.
3. **Defect Report** (`DefectReport.docx`): Prepare a formal defect report documenting bug ID, description, steps to reproduce, severity, priority, expected vs actual result, including screenshots.
4. **Selenium Grid & WebDriver Setup** (`GridTest.java`): Install Selenium Grid, WebDriver, execute sample automated tests.
5. **Software Requirement Specification (SRS)** (`SRS_LibraryManagementSystem.docx`): Prepare an SRS document for a sample project, e.g., Library Management System.

---

## Requirements

- **Python 3.x** (ML & CSDF scripts)
- **C++ Compiler** (DAA)
- **Java JDK 17+** (STQA)
- **Eclipse IDE** (Java & Web Developers)
- **Selenium WebDriver 4.x** (STQA)
- **Chrome / ChromeDriver** (STQA)
- **Optional:** XAMPP for local HTML testing (STQA)

---

## How to Run

- **ML:** Open `.ipynb` files in Jupyter Notebook; ensure required libraries (`numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `tensorflow`) are installed.
- **DAA (C++):** Compile using `g++` and run executables.  
  **Python:** Run `knapsack.py` and `nqueens.py` using Python.
- **CSDF:** Run Python scripts with required input files (`header.txt`, `image.dd`, log files).  
- **STQA:** Run Java programs in Eclipse or via Maven; open `.docx` files for defect reports and SRS.

---

## Notes

- Ensure **browser driver versions match installed browsers** for Selenium tests.
- Use **Maven** to manage Java dependencies for STQA.
- Include **Excel outputs, SRS documents, screenshots, and code files** in practical submissions.
- This repository is for **educational purposes only**.

---

✍️ Prepared for **SPPU BE Computer Engineering – Semester 7**
