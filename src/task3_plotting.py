import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the plotting functions
def plot_1d(data):
    plt.figure(figsize=(8, 5))
    plt.plot(data, label='1D Line Plot')
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("1D Line Plot of Data Sequence")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_2d(x, y):
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='b', label='2D Scatter Plot')
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.title("2D Scatter Plot of X vs Y")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_3d(x, y, z):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='r', label='3D Scatter Plot')
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("3D Scatter Plot of X, Y, Z Data")
    plt.legend()
    plt.show()

# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Plot each type of data
plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
