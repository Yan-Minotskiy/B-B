import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import graphs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Анализ сетевого трафика'),
    # html.P(children='Проанализировано ' + graphs.analyzed + ' пакетов'),
    #tml.H2(children=graphs.input_traffic),
    #html.H2(children=graphs.output_traffic),
    #html.Div(children=[dcc.Graph(id='traffic_time', figure=graphs.traffic_time)]),
    html.Div(children=[dcc.Graph(id="proto_pie", figure=graphs.proto_pie)]),
    html.Div(children=[dcc.Graph(id="geo_pie", figure=graphs.geo_pie)]),
    html.Div(children=[dcc.Graph(id='traffic_map', figure=graphs.traffic_map)])

])

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')