
# K-Nearest Neighbors (KNN) Classification on Iris Dataset

This project demonstrates how to implement and visualize the K-Nearest Neighbors (KNN) algorithm on the Iris dataset using Python and scikit-learn.

---

##  Dataset

**Source**: [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

- **Features**:
  - SepalLengthCm
  - SepalWidthCm
  - PetalLengthCm
  - PetalWidthCm
- **Target**:
  - Species (Setosa, Versicolor, Virginica)

---

##  Project Steps

### 1. Data Preprocessing
- Loaded the Iris dataset from CSV
- Removed the `Id` column
- Encoded the `Species` labels using LabelEncoder
- Standardized the feature values using `StandardScaler`

### 2. KNN Model Training
- Split the data into training and test sets (80/20 split)
- Trained a `KNeighborsClassifier` using different values of K
- Evaluated using:
  - **Accuracy Score**
  - **Confusion Matrix**

### 3. K Value Experimentation
- Tested K values from 1 to 20
- Visualized the accuracy for each value of K using a line plot

### 4. Decision Boundary Visualization
- Selected the first two standardized features for 2D visualization
- Plotted decision boundaries using `matplotlib` and `ListedColormap`
- Showed how the classifier separates classes in feature space

---

##  Sample Results

- Accuracy ~96-100% for optimal K values
- Clear separation of species in decision boundary plot
- Confusion matrix showing low misclassification

---

##  Requirements

- Python 3.x
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

```bash
pip install pandas numpy matplotlib seaborn scikit-learn

