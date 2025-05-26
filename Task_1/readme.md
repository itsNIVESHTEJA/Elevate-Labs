## Project Flow

### 1. Data Loading
- Loaded the dataset using `pandas` for analysis.

### 2. Data Cleaning
- Checked for null values.
- Filled missing values in `Age` and `Embarked`.
- Dropped irrelevant or sparse columns like `Cabin`, `Ticket`, and `Name`.

### 3. Exploratory Data Analysis (EDA)
-normalization
 -using standardscaler
- Univariate analysis using:
  - Count  (e.g., `Sex``)
 - Bivariate and multivariate analysis using:
  - Box plots (Age )
- detect outliers with boxplot
  -remove it by using IQR
##  Libraries Used

- `pandas`, `numpy` – data handling
- `matplotlib` – data visualization
- `sklearn` – machine learning and evaluation,normalization,split the data
