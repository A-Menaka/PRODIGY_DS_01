# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris dataset (make sure to have it in your working directory or provide the correct path)
df = pd.read_csv('iris.csv')  # Replace 'iris.csv' with the correct path if needed

# For a histogram of sepal_length (continuous variable)
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], kde=True, bins=10)
plt.title('Sepal Length Distribution')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# For a bar chart of species (categorical variable)
species_counts = df['species'].value_counts()
plt.figure(figsize=(6, 6))
species_counts.plot(kind='bar')
plt.title('Species Distribution')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()


