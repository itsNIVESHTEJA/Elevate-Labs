
# Logistic Regression on Breast Cancer Dataset

This project demonstrates a complete binary classification pipeline using **Logistic Regression** on the **Breast Cancer Wisconsin Diagnostic Dataset**. It covers all essential preprocessing and evaluation steps to build a robust model for predicting whether a tumor is benign or malignant.

---

## Problem Statement

To predict whether a tumor is **benign (B)** or **malignant (M)** based on various features such as radius, texture, perimeter, area, and more.

---

##  Dataset Summary

- **Instances**: 569
- **Features**: 30 numeric, 1 target (`diagnosis`)
- **Target Classes**: 
  - `M` = Malignant
  - `B` = Benign

---

## Workflow Overview

### 1. Exploratory Data Analysis (EDA)
- Understand data structure, missing values, and class distribution.
- Visualize correlations and distributions (optional for extension).

### 2. Data Cleaning
- Remove irrelevant columns like `id`.
- Drop missing or duplicate rows.

### 3. Outlier Detection & Handling
- Apply IQR method to remove outliers from key numeric features.

### 4. Skewness Correction
- Use log transformation (`log1p`) to normalize highly skewed features.

### 5. Encoding
- Convert categorical target `diagnosis` to binary (`M`=1, `B`=0) using Label Encoding.

### 6. Feature Scaling
- Standardize all numeric features using `StandardScaler`.

### 7. Modeling
- Train a **Logistic Regression** model on the training data.

### 8. Model Evaluation
- Evaluate using:
  - Confusion Matrix
  - Precision & Recall
  - ROC Curve & AUC Score

### 9. Threshold Tuning
- Adjust classification threshold (default 0.5 → custom e.g., 0.3) to observe precision-recall trade-off.

---

## 🧠 Key Concepts

- **Logistic Regression**: Used for binary classification by mapping input features to a probability using the **sigmoid function**.
  
- **Sigmoid Function**:  
  \\[
  \\sigma(z) = \\frac{1}{1 + e^{-z}}
  \\]  
  Maps linear combinations to probabilities between 0 and 1.

---

## Outcome

A well-preprocessed and tuned logistic regression model capable of accurately classifying tumors with a good balance of precision and recall.

---


##  Requirements

- Python 
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`


