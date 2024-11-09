import matplotlib.pyplot as plt
import numpy as np
import collections

def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    # Count frequency of each category
    counter = collections.Counter(data)
    categories = list(counter.keys())
    frequencies = list(counter.values())
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(categories, frequencies, color=['skyblue', 'salmon', 'lightgreen'])
    
    # Labeling the chart
    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Each Category')
    plt.show()
    
    return fig

# Generate example data
data = np.random.choice(['A', 'B', 'C'], size=100)

# Plot the distribution
plot_distribution(data)
