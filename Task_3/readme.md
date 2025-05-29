# Housing Price Prediction

This project uses **Linear Regression** to predict housing prices based on various features like area, number of bedrooms, parking availability, and location-related attributes.

---

##  Dataset

The dataset used is `Housing.csv` and contains the following columns:

- `price`: Target variable (house price)
- `area`: Size of the house
- `bedrooms`, `bathrooms`, `stories`, `parking`: Numerical features
- `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`: Binary categorical features
- `furnishingstatus`: Multi-category categorical feature

---

##  Data Preprocessing

### 1. Import Dataset
The dataset is imported using a data manipulation library such as pandas.

### 2. Skewness Correction
To handle skewed distributions in the numeric features, log transformation is applied using the `log1p` method. Numeric columns with skewness greater than 0.5 are selected and transformed. This helps stabilize variance and improve model performance.

### 3. Handle Categorical Variables
All categorical features are encoded into numerical form using label encoding to make them suitable for model training.
---

##  Model Building

### 1. Train-Test Split
The dataset is divided into training and testing sets to evaluate the model’s performance on unseen data.

### 2. Model Selection
Linear Regression is chosen as the algorithm to model the relationship between features and the target variable (house price).

### 3. Model Training
The model is trained on the training dataset using the selected features.

### 4. Model Evaluation
The model is evaluated using metrics such as R² Score and RMSE to measure its accuracy and error.

---

## ✅ Conclusion

- Linear Regression provides a baseline model for predicting housing prices.
- Log transformation of skewed numeric features improves the model’s predictive ability.
- The model can be further enhanced using more advanced algorithms, feature scaling, and cross-validation.

---

## 📦 Requirements

- Python
- pandas
- numpy
- scikit-learn
- matplot lib

