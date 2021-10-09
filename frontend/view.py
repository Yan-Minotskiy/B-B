import os
import pathlib
import numpy as np
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from scipy.stats import rayleigh


GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 5000)

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.title = "Анализ сетевого трафика"

server = app.server

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

app.layout = html.Div([
    # header
    html.Div([
        html.Div([
            html.H1("АНАЛИЗ СЕТЕВОГО ТРАФИКА", className="app__header__title"),
            html.P("Это приложение проводит анализ сетевого трафика проходящего через ваше устройство.",
            className="app__header__title--grey"),
        ], className="app__header__desc")
    ], className="app__header"),
    # здесь ещё можно добавить наиболее важные цифровые показатели
    
    # input_trffic_graph
    html.Div([
        html.Div([
            html.Div([
                html.H6("ВХОДЯЩИЙ ТРАФИК", className="graph__title")]),
                        dcc.Dropdown(
                            id='xaxis-column',
                            options=[{'label': i, 'value': i} for i in ['График скорости трафика', 'Доля source ip address', 'Карта входящего трафика']],
                            value='График скорости трафика'
                        ),
                        dcc.Graph(
                            id="wind-speed",
                            figure=dict(
                                layout=dict(
                                    plot_bgcolor=app_color["graph_bg"],
                                    paper_bgcolor=app_color["graph_bg"],
                                )
                            ),
                        ),
                        dcc.Interval(
                            id="wind-speed-update",
                            interval=int(GRAPH_INTERVAL),
                            n_intervals=0,
                        ),
        ])]
    ),

    # output_traffic_graph
    html.Div([
        html.Div([
            html.Div([
            html.H6("ИСХОДЯЩИЙ ТРАФИК", 
            className="graph__title")]
                        ),
                        dcc.Graph(
                            id="pass",
                            figure=dict(
                                layout=dict(
                                    plot_bgcolor=app_color["graph_bg"],
                                    paper_bgcolor=app_color["graph_bg"],
                                )
                            ),
                        ),
                        dcc.Interval(
                            id="pass1",
                            interval=int(GRAPH_INTERVAL),
                            n_intervals=0,
                        ),
        ])]
    ),
], className="app__container")

if __name__ == "__main__":
    app.run_server(debug=True)