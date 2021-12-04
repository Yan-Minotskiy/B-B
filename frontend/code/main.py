import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

import graphs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(children=[
    html.H1(children='Анализ сетевого трафика'),
    html.Div([
    dcc.Graph(
        id='example-graph1',
        figure=graphs.fig_map),
    dcc.Graph(
        id='example-graph2',
        figure=graphs.pie_country)
    ], style={'columnCount': 2})
    ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')