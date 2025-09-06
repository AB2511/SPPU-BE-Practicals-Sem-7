# SPPU BE Projects Semester 7 - Machine Learning (LP3)

This repository contains implementations for Machine Learning assignments as part of the LP3 (Lab Practice 3) course in Semester 7 of BE (Bachelor of Engineering) at Savitribai Phule Pune University (SPPU). The assignments cover various ML concepts and algorithms. Only Jupyter Notebook (.ipynb) files are pushed to GitHub, along with the required datasets.

Datasets for the assignments have been uploaded to this repository for convenience.

## Assignments Overview

### Assignment 1: Uber Ride Price Prediction
- **File**: `MLAssignment1.ipynb`
- **Description**: Predict the price of an Uber ride from a given pickup point to the drop-off location.
- **Tasks**:
  1. Pre-process the dataset.
  2. Identify outliers.
  3. Check the correlation.
  4. Implement linear regression and random forest regression models.
  5. Evaluate the models and compare scores (R2, RMSE).
- **Dataset**: `uber.csv` (from [Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)).

### Assignment 2: Bank Customer Churn Prediction
- **File**: `MLAssignment2.ipynb`
- **Description**: Build a neural network-based classifier to predict if a bank customer will leave in the next 6 months.
- **Tasks**:
  1. Read the dataset.
  2. Distinguish features and target; split into training/test sets.
  3. Normalize the data.
  4. Initialize and build the model; identify improvements.
  5. Print accuracy score and confusion matrix.
- **Dataset**: `Churn_Modelling.csv` (from [Kaggle](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)).

### Assignment 3: Gradient Descent Algorithm
- **File**: `MLAssignment3.ipynb`
- **Description**: Implement Gradient Descent to find the local minima of the function \( y = (x + 3)^2 \), starting from \( x = 2 \).
- **Tasks**: Implement the algorithm with convergence criterion and plot the descent path.
- **Dataset**: None (algorithm implementation).

### Assignment 4: K-Nearest Neighbors on Diabetes Dataset
- **File**: `MLAssignment4.ipynb`
- **Description**: Implement K-Nearest Neighbors on the diabetes dataset and compute confusion matrix, accuracy, error rate, precision, and recall.
- **Tasks**: Pre-process data, train KNN, evaluate metrics.
- **Dataset**: `diabetes.csv` (from [Kaggle](https://www.kaggle.com/datasets/abdallamahgoub/diabetes)).

## Requirements
To run the notebooks, you'll need Python 3.x and the following libraries. Install them using `pip`:

```
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
```

- **Environment**: Python 3.12.7 (as used in the notebooks).
- Note: For Assignment 2, TensorFlow is required for the neural network.

## How to Run
1. Clone the repository:  
   ```
   git clone https://github.com/AB2511/SPPU-BE-Practicals-Sem-7.git
   ```
2. Navigate to the ML folder:  
   ```
   cd SPPU-BE-Practicals-Sem-7/ML
   ```
3. Open Jupyter Notebook:  
   ```
   jupyter notebook
   ```
4. Select and run the desired .ipynb file. Datasets are included in the repo, so no external downloads are needed.

## Notes
- These assignments are for educational purposes only.
- If you encounter issues with notebook rendering on GitHub, download and run locally via Jupyter.
- Datasets are sourced from Kaggle and used under their terms.

