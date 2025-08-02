# 🌸 Iris Dataset - Exploratory Data Analysis (EDA)

This project provides a comprehensive Exploratory Data Analysis (EDA) of the classic Iris dataset, widely used in pattern recognition and machine learning. The goal is to uncover meaningful patterns, visualize relationships between features, and highlight the differences between the three species of Iris flowers: Setosa, Versicolor, and Virginica.

---

## 📌 Project Objective

The primary objective of this project is to:
- Analyze the characteristics of the Iris dataset.
- Understand the distribution and variance of each flower feature (Sepal/Petal length and width).
- Visualize inter-feature relationships and differences between flower species.
- Derive key insights using data visualization techniques.

This EDA lays the foundation for building classification models and better understanding real-world datasets.

---

## 🧰 Technologies Used

| Tool / Library | Purpose |
|----------------|---------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **Matplotlib** | Static plotting and charting |
| **Seaborn** | Statistical visualizations |
| **Scikit-learn** | Dataset loading utility (`load_iris()` function) |

---

## 📂 Dataset Information

- **Source:** `sklearn.datasets.load_iris()`
- **Total Samples:** 150
- **Features:**
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- **Target Classes:**  
  - Setosa  
  - Versicolor  
  - Virginica

---

## 📊 Visualizations Created

Each visualization helps to uncover patterns in the dataset:

- ✔️ **Pairplot** – Displays relationships between every pair of features across all species.
- ✔️ **Histogram** – Shows feature distributions (e.g., petal lengths of different species).
- ✔️ **Boxplot** – Highlights median, IQR, and outliers in each feature grouped by species.
- ✔️ **Heatmap** – Displays correlation between features using color-coded matrix.

---

## 🧠 Key Insights

- 🌱 **Setosa is highly distinguishable:**  
  Easily identified due to consistently small petal dimensions. Forms a tight, unique cluster in pairplots.

- 🌺 **Strong correlation in Petal features:**  
  Petal Length and Petal Width show a high positive correlation, indicating linked growth patterns.

- 🍃 **Versicolor vs. Virginica overlap:**  
  Some overlapping distributions, especially in Sepal features. These may require more advanced classification techniques.

- 🌿 **Low correlation between Sepal Length and Width:**  
  Indicates independence of these features.

---

## 📸 Output Visualizations

Below are the key visualizations generated during the EDA:

### 1️⃣ Pairplot - Feature Relationship
![Pairplot](images/screenshot.jpg)

### 2️⃣ Heatmap - Feature Correlation
![Heatmap](images/screenshot.png)

### 3️⃣ Histograms - Feature Distributions
![Histograms](images/screenshot1.png)

### 4️⃣ Boxplot - Feature Spread & Outliers
![Boxplot](images/screenshot2.png)
