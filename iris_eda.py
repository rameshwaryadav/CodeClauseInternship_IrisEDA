import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_raw = load_iris()

df = pd.DataFrame(data=iris_raw.data, columns=iris_raw.feature_names)
df['species'] = pd.Categorical.from_codes(iris_raw.target, iris_raw.target_names)

print("First 5 Rows of the Dataset:")
print(df.head())

print("\nDataset Info:")
df.info()

sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8-talk')

sns.pairplot(df, hue='species', palette='viridis', markers=["o", "s", "D"])
plt.suptitle('Pairplot of Iris Dataset by Species', y=1.02)
plt.show()

df.hist(figsize=(12, 10), bins=20, edgecolor='black')
plt.suptitle('Histogram for Each Feature', y=1.02)
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(data=df, orient='h', palette='pastel')
plt.title('Boxplot for All Features to See Spread and Outliers')
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Boxplot of Features by Species', y=1.02)

sns.boxplot(ax=axes[0, 0], x='species', y='sepal length (cm)', data=df)
axes[0, 0].set_title('Sepal Length by Species')

sns.boxplot(ax=axes[0, 1], x='species', y='sepal width (cm)', data=df)
axes[0, 1].set_title('Sepal Width by Species')

sns.boxplot(ax=axes[1, 0], x='species', y='petal length (cm)', data=df)
axes[1, 0].set_title('Petal Length by Species')

sns.boxplot(ax=axes[1, 1], x='species', y='petal width (cm)', data=df)
axes[1, 1].set_title('Petal Width by Species')

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.show()

numeric_df = df.drop('species', axis=1)
correlation_matrix = numeric_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap of Iris Features')
plt.show()
