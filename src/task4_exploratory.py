import pandas as pd
import seaborn as sns

# Define the EDA function
def perform_eda(df):
    # Descriptive Statistics
    descriptive_stats = df.describe().T
    descriptive_stats['median'] = df.median()
    descriptive_stats['mode'] = df.mode().iloc[0]
    display(descriptive_stats)
    
    # Box Plot for Outlier Detection
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, palette="Set2")
    plt.title("Box Plot for Outlier Detection")
    plt.ylabel("Values")
    plt.show()
    
    # Correlation Matrix and Heatmap
    correlation_matrix = df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix Heatmap")
    plt.show()

# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})

# Perform EDA on the dataset
perform_eda(df)
