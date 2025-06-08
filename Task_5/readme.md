#  Heart Disease Classification using Decision Tree & Random Forest

This project analyzes heart disease data to classify patients as having or not having heart disease using machine learning models: **Decision Tree** and **Random Forest**.

##  Dataset

- File: `heart.csv`
- Target column: `target` (1 = disease, 0 = no disease)
- Features include: age, sex, chest pain type, resting blood pressure, cholesterol, etc.

---

##  Steps Covered

### 1. Load and Explore the Data
- Use `pandas` to load the CSV.
- Check for null values, datatypes, and class distribution.

### 2. Decision Tree Classifier
- Trained a `DecisionTreeClassifier` on the dataset.
- Visualized the decision tree using `plot_tree`.
- Observed how the tree splits data to make predictions.

### 3. Overfitting Analysis
- Controlled model complexity using `max_depth`.
- Compared training vs testing accuracy for different depths.
- Noted overfitting when the depth is too high.

### 4. Random Forest Classifier
- Trained a `RandomForestClassifier` with 100 trees.
- Compared accuracy with Decision Tree.
- Random Forest performs better due to ensemble voting.

### 5. Feature Importance
- Visualized the most important features contributing to prediction using bar plots.
- Identified key indicators like chest pain type, thal, oldpeak, and cp.

### 6. Cross-Validation
- Performed 5-fold cross-validation on the Random Forest model.
- Calculated average accuracy to ensure model generalization.

---

## 🛠️ Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- scikit-learn

Install with:

```bash
pip install pandas matplotlib seaborn scikit-learn

