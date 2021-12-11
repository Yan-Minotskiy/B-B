import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import graphs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Анализ сетевого трафика', style={'text-align': 'center'}),
    # добавить фильтров
    html.Div([
    ]),
    html.Div(id='control', children=[]),
    dcc.Tabs(id="tabs", value='stats', children=[
        dcc.Tab(label='Статистика', value='stats'),
        dcc.Tab(label='Протоколы', value='proto'),
        dcc.Tab(label='IP адреса', value='ip_list'),
        dcc.Tab(label='MAC адреса', value='mac_list'),
        dcc.Tab(label='География', value='geo')
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'stats':
        return html.Div([
            html.H2('Основная информация о трафике', style={'text-align': 'center'}),
            html.P('Всего проанализировано пакетов: {analyzed}'.format(analyzed=graphs.analyzed),
                   style={
                       'font-weight': 'bold',
                       'text-align': 'center'
                   }
                   )
        ])
    elif tab == 'proto':
        return html.Div([
            html.H2('Информация о протоколах передачи', style={'text-align': 'center'}),
            html.Div(children=[dcc.Graph(id="proto_pie", figure=graphs.proto_pie)]),
            html.Details([
                html.Summary('Справка по протоколам'),
                html.P([
                    html.Span('TCP', style={'font-weight': 'bold'}),
                    """
                     — один из основных протоколов передачи данных интернета. 
                    Предназначен для управления передачей данных интернета. 
                    Медленнее и надёжнее UDP.
                    """
                ]),
                html.P([
                    html.Span('UDP', style={'font-weight': 'bold'}),
                    """
                     - один из ключевых элементов набора сетевых протоколов для Интернета. 
                    С UDP компьютерные приложения могут посылать сообщения другим хостам по IP-сети 
                    без необходимости предварительного сообщения для установки специальных каналов передачи или путей данных.
                    Быстрый и менее надёжный в сравнении с TCP
                    """
                ]),
                html.P([
                    html.Span('ICMP', style={'font-weight': 'bold'}),
                    """
                     — протокол межсетевых управляющих сообщений. 
                    Используется для передачи сообщений об ошибках и других исключительных ситуациях, возникших при передаче данных хост. 
                    Также на ICMP возлагаются некоторые сервисные функции.
                    """
                ]),
            ])
        ])
    elif tab == 'ip_list':
        return html.Div([
            html.H2('IP адреса', style={'text-align': 'center'}),  # поставить по центру
            html.P('IP адрес прослушиваемого интерфеса: {ip}'.format(ip=graphs.IP_addres),
                   style={'font-weight': 'bold'}),
            dcc.Input(
                placeholder='8.8.8.8',
                type='text',
                value=''
            ),
            html.Button('Найти', id='button')
            # реализовать таблицу
        ])
    elif tab == 'mac_list':
        return html.Div([
            html.H2('MAC адреса', style={'text-align': 'center'}),
            html.P('MAC адрес устройства: {mac}'.format(mac=graphs.mac),
                   style={'font-weight': 'bold'}
                   )
        ])
    elif tab == 'geo':
        return html.Div([
            html.H2('География трафика', style={'text-align': 'center'}),
            html.Div(children=[dcc.Graph(id='geo_pie', figure=graphs.geo_pie)]),
            html.Div(children=[dcc.Graph(id='traffic_map', figure=graphs.traffic_map)])
        ])


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')
