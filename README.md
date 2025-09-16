# SPPU BE Practicals Semester 7

This repository contains practical implementations for Semester 7 BE (Bachelor of Engineering) at Savitribai Phule Pune University (SPPU), covering **Machine Learning (ML)**, **Design and Analysis of Algorithms (DAA)**, and **Cyber Security & Digital Forensics (CSDF)**.  
The assignments include Jupyter Notebooks, Python scripts, and C++ files, along with required datasets where applicable. All code is for educational purposes only.

---

## Subjects and Assignments

### Machine Learning (ML)
- **Folder**: `ML`
- **Assignments**:
  1. **Uber Ride Price Prediction** (`MLAssignment1.ipynb`): Predict Uber ride prices using linear and random forest regression. Dataset: `uber.csv` ([Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)).
  2. **Bank Customer Churn Prediction** (`MLAssignment2.ipynb`): Build a neural network classifier. Dataset: `Churn_Modelling.csv` ([Kaggle](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)).
  3. **Gradient Descent Algorithm** (`MLAssignment3.ipynb`): Find local minima of \( y = (x + 3)^2 \) with plotting.
  4. **K-Nearest Neighbors on Diabetes** (`MLAssignment4.ipynb`): Implement KNN and compute metrics. Dataset: `diabetes.csv` ([Kaggle](https://www.kaggle.com/datasets/abdallamahgoub/diabetes)).

---

### Design and Analysis of Algorithms (DAA)
- **Folder**: `DAA`
- **Assignments**:
  1. **Fibonacci Numbers with Step Count**:
     - `Fibononrecur.cpp` (Non-recursive)
     - `Fiborecur.cpp` (Recursive)
  2. **Fractional Knapsack Problem** (`knapsack.py`): Solve using greedy method.
  3. **0-1 Knapsack Problem** (`knapsack01.cpp`): Solve using dynamic programming.
  4. **8-Queens Problem with Backtracking** (`nqueens.py`): Place queens on an 8x8 board.

---

### Cyber Security & Digital Forensics (CSDF – LP4)
- **Folder**: `CSDF`
- **Assignments**:
  1. **Tracking Emails & Investigating Email Crimes**  
     - `textCaptcha.py`, `header.txt`  
     - Parses raw email headers (MIME, Date, Subject, From, To, Received). Helps trace origins of suspicious emails.  
  2. **CAPTCHA Generation & Verification**  
     - `textCaptcha.py`, `imgCaptcha.py`  
     - Generates random alphanumeric CAPTCHA strings and verifies user input.  
     - Produces CAPTCHA images (`CAPTCHA.png`) using the `captcha` library.  
  3. **Recovering Permanently Deleted Files and Partitions**  
     - `recover_files.py`, `scan_partitions.py`, `image.dd`  
     - Recovers deleted JPG/PNG/PDF files from raw disk images using file carving.  
     - Scans disk images for partition signatures (MBR, NTFS, FAT32).  
  4. **Log Correlation**  
     - `log_correlation.py`, `server1.log`, `server2.log`  
     - Parses and correlates multiple log files. Detects events (e.g., warnings) that occur close in time across systems.  

---

## Requirements
- **Python 3.x** with libraries:
  - ML: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `tensorflow`
  - CSDF: `captcha`, `Pillow`
- **C++ Compiler** (e.g., g++) for DAA C++ files

---

## How to Run

### Clone the Repository
```

git clone [https://github.com/AB2511/SPPU-BE-Practicals-Sem-7.git](https://github.com/AB2511/SPPU-BE-Practicals-Sem-7.git)

````

---

### Machine Learning (ML)
```bash
cd SPPU-BE-Practicals-Sem-7/ML
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
jupyter notebook
````

Run the desired `.ipynb` file. Datasets are included.

---

### Design and Analysis of Algorithms (DAA)

```bash
cd SPPU-BE-Practicals-Sem-7/DAA
```

#### For C++ Files

```bash
g++ Fibononrecur.cpp -o fib_non_recur
g++ Fiborecur.cpp -o fib_recur
g++ knapsack01.cpp -o knapsack01

./fib_non_recur
./fib_recur
./knapsack01
```

#### For Python Files

```bash
python knapsack.py
python nqueens.py
```

---

### Cyber Security & Digital Forensics (CSDF – LP4)

```bash
cd SPPU-BE-Practicals-Sem-7/CSDF
```

#### Assignment 1 – Email Header Analysis

```bash
python textCaptcha.py
# Enter path to header.txt when prompted
```

#### Assignment 2 – CAPTCHA

```bash
python textCaptcha.py
python imgCaptcha.py
```

#### Assignment 3 – File/Partition Recovery

```bash
python scan_partitions.py image.dd
python recover_files.py image.dd recovered_files
```

#### Assignment 4 – Log Correlation

```bash
python log_correlation.py
```

---

## Notes

* Datasets for ML are sourced from Kaggle and included in the repo.
* `image.dd` in CSDF can be created manually or downloaded from **Digital Corpora**.
* Outputs may vary depending on inputs and test files.
* This repository is for **educational purposes only** (SPPU Semester 7 Practicals).

---
✍️ Prepared for **SPPU BE Computer Engineering – Semester 7**
