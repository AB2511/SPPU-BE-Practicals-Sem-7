# SPPU BE Practicals Semester 7

This repository contains practical implementations for Semester 7 BE (Bachelor of Engineering) at Savitribai Phule Pune University (SPPU), covering **Machine Learning (ML)** and **Design and Analysis of Algorithms (DAA)**. The assignments include Jupyter Notebooks, Python scripts, and C++ files, along with required datasets where applicable. All code is for educational purposes only.

## Subjects and Assignments

### Machine Learning (ML)
- **Folder**: `ML`
- **Assignments**:
  1. **Uber Ride Price Prediction** (`MLAssignment1.ipynb`): Predict Uber ride prices using linear and random forest regression. Dataset: `uber.csv` ([Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)).
  2. **Bank Customer Churn Prediction** (`MLAssignment2.ipynb`): Build a neural network classifier. Dataset: `Churn_Modelling.csv` ([Kaggle](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)).
  3. **Gradient Descent Algorithm** (`MLAssignment3.ipynb`): Find local minima of \( y = (x + 3)^2 \) with plotting.
  4. **K-Nearest Neighbors on Diabetes** (`MLAssignment4.ipynb`): Implement KNN and compute metrics. Dataset: `diabetes.csv` ([Kaggle](https://www.kaggle.com/datasets/abdallamahgoub/diabetes)).

### Design and Analysis of Algorithms (DAA)
- **Folder**: `DAA `
- **Assignments**:
  1. **Fibonacci Numbers with Step Count**:
     - `Fibononrecur.cpp` (Non-recursive)
     - `Fiborecur.cpp` (Recursive)
  2. **Fractional Knapsack Problem** (`knapsack.py`): Solve using greedy method.
  3. **0-1 Knapsack Problem** (`knapsack01.cpp`): Solve using dynamic programming.
  4. **8-Queens Problem with Backtracking** (`nqueens.py`): Place queens on an 8x8 board.

## Requirements
- **Python 3.x** with libraries:
  - ML: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `tensorflow`
  - DAA: No additional libraries needed
- **C++ Compiler** (e.g., g++) for DAA C++ files

## How to Run

### Clone the Repository
```
git clone https://github.com/AB2511/SPPU-BE-Practicals-Sem-7.git
```

### Machine Learning (ML)
1. Navigate to the ML folder:
   ```
   cd SPPU-BE-Practicals-Sem-7/ML
   ```
2. Install dependencies:
   ```
   pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
   ```
3. Open Jupyter Notebook:
   ```
   jupyter notebook
   ```
4. Run the desired `.ipynb` file. Datasets are included.

### Design and Analysis of Algorithms (DAA)
1. Navigate to the DAA folder:
   ```
   cd SPPU-BE-Practicals-Sem-7/DAA
   ```

#### For C++ Files (`Fibononrecur.cpp`, `Fiborecur.cpp`, `knapsack01.cpp`)
- Compile:
  ```
  g++ Fibononrecur.cpp -o fib_non_recur
  g++ Fiborecur.cpp -o fib_recur
  g++ knapsack01.cpp -o knapsack01
  ```
- Run:
  ```
  ./fib_non_recur
  ./fib_recur
  ./knapsack01
  ```
- Input values when prompted for Fibonacci files.

#### For Python Files (`knapsack.py`, `nqueens.py`)
- Run:
  ```
  python knapsack.py
  python nqueens.py
  ```
- For `nqueens.py`, enter row and column (0-7) for the first queen.

## Notes
- Datasets for ML are sourced from Kaggle and included in the repo.
- Outputs may vary based on input (e.g., Fibonacci count, queen position).
- Refer to assignment files for detailed tasks and expected outputs.
- **Up-to-Date**: Incorporates the current date (September 06, 2025) implicitly through the context of the repository activity.

This combined README serves as a central entry point for both subjects, guiding users to the respective folders for detailed exploration.
