import dash
from dash import dcc
from dash.dependencies import Input, Output
from dash import html
import pandas as pd
import plotly.express as px
import graphs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Анализ сетевого трафика'),
    html.Div([
        dcc.Dropdown(
        options=[
            {'label': 'TCP', 'value': 'tcp'},
            {'label': 'UDP', 'value': 'udp'},
            {'label': 'ICMP', 'value': 'icmp'}
        ],
        multi=True,
        value=['tcp', 'udp', 'icmp']
    )
    ]),
    html.Div(id="control", children=[]),
    dcc.Tabs(id="tabs", value='stats', children=[
        dcc.Tab(label='Статистика', value='stats'),
        dcc.Tab(label='Протоколы', value='proto'),
        dcc.Tab(label='Список IP', value='ip_list'),
        dcc.Tab(label='Список MAC', value='mac_list'),
        dcc.Tab(label='География', value='geo'),
        dcc.Tab(label='Поиск по IP', value='search'),
    ]),
    html.Div(id='tabs-content'),
    #html.Div(id='footer', children=[html.P('B-B Team. Москва. 2021'),], 
    #         style={'backgraund': 'blue'})
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'proto':
        return html.Div([
            html.Div(children=[dcc.Graph(id="proto_pie", figure=graphs.proto_pie)])
        ])
    elif tab == 'geo':
        return html.Div([
            html.Div(children=[dcc.Graph(id="geo_pie", figure=graphs.geo_pie)]),
            html.Div(children=[dcc.Graph(id='traffic_map', figure=graphs.traffic_map)])
        ], style={'columns': 2})
    elif tab == 'search':
        return html.Div([
            html.H2('Поиск по IP адресу'),
            dcc.Input(
                placeholder='8.8.8.8',
                type='text',
                value=''
            ),
            html.Button('Найти', id='button')
        ])
    else:
        return html.H2(children='Здесь пока пусто')


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')