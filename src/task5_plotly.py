import plotly.express as px

# Define the function to create an interactive Plotly scatter plot
def create_interactive_plotly(df):
    fig = px.scatter(
        df, x='x', y='y',
        title="Interactive Scatter Plot",
        labels={"x": "X Axis", "y": "Y Axis"},
    )
    fig.update_layout(legend_title="Legend", title_x=0.5)
    fig.show()

# Example data
df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})

# Create and display the interactive Plotly scatter plot
create_interactive_plotly(df)
