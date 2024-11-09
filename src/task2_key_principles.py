import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Set the Seaborn style for clarity and simplicity
    sns.set_style("whitegrid")
    
    # Create the scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x='x', y='y', ax=ax, color='dodgerblue')
    
    # Labeling the plot
    ax.set_xlabel('Variable X')
    ax.set_ylabel('Variable Y')
    ax.set_title('Scatter Plot of Variables X and Y')
    
    plt.show()
    return fig

# Generate example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})

# Create the scatter plot
create_scatter_plot(data)
