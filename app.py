import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
import pandas as pd

df = pd.read_csv('home run data.csv')
x = df["Player"]
y = df["Launch Angle"]
z = df["Exit Velocity (MPH)"]
rounds = df["Distance (Ft.)"]

app = dash.Dash(
    __name__,
    external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

server = app.server

app.layout = html.Div([
    dcc.Markdown("""
## Home Run Derby: HRs by Distance, Exit Velocity, and Launch Angle

##### The color represents the distance. darker red = longer, lighter color = shorter.
"""),
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
                    yaxis=dict(title="Launch Angle"),
                    zaxis=dict(title="Exit Velocity")
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