import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
import pandas as pd

df = pd.read_csv('/Users/rromney/Desktop/home run data.csv')
x = df["Player"]
y = df["Distance (Ft.)"]
z = df["Exit Velocity (MPH)"]
rounds = df["Launch Angle"]

app = dash.Dash(
    __name__,
    external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div([
    dcc.Markdown("""## Home Run Derby: HRs by Distance, Exit Velocity, and Launch Angle"""),
    dcc.Graph(
       figure = go.Figure(
            data = [
                go.Scatter3d(
                    x = x,
                    y = y,
                    z = z,
                    hoverinfo='x, y, z',
                    mode="markers",
                    marker=dict(
                        size=12,
                        color=rounds,
                        opacity=.8,
                    ),        
                )
            ],
            layout = go.Layout(
                height=900,    
                scene=dict(
                    xaxis=dict(title="Launch Angle"),
                    yaxis=dict(title="Distance"),
                )
            )
       ),
       style=dict(maxWidth="1000px",margin='auto')
    ),
    dcc.Markdown(
"""
___

Made with ❤️ by [Russell](https://github.com/russellromney)
""")
],style=dict(width="100vw",textAlign='center'))


if __name__ == "__main__":
    app.run_server()