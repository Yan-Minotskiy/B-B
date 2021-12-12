import socket
import uuid

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine

import config

# устанавливаем соединение с базой данных
engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(config.database["user"],
                                                            config.database["password"],
                                                            config.database["host"],
                                                            config.database["port"],
                                                            config.database["database"]))

# импортируем данные из таблиц
frame = pd.read_sql_table("frame", engine)
ip_location = pd.read_sql_table("ip_location", engine)

# вычисление показателей
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
analyzed = frame.shape[0]  # количество проанализированных пакетов
ip = socket.gethostbyname(h_name)
mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
input_traffic = frame.loc[frame['d_ip'] == ip].shape[0]
output_traffic = frame.loc[frame['s_ip'] == ip].shape[0]
merge_df = frame.merge(ip_location, left_on='s_ip', right_on='ip', how='inner')
# merge_df['count'] = merge_df.loc[merge_df['s_ip'] == merge_df['s_ip']].shape[0]
# frame['s_ip'].value_counts(ascending=False)

# информация о протоколах подключения
proto_count = frame.groupby('protocol').count()
protocols = list(proto_count.index)
count_protocols = list(proto_count.id)

# Ip адреса
ip_count = frame.groupby('s_ip').count()

# traffic_time = px.bar(frame, x='arrival_time')

# круговая диагрмма протоколов
proto_pie = go.Figure(data=[go.Pie(labels=protocols, values=count_protocols, hole=.5)])

traffic_count = frame.groupby('type').count()
types = list(traffic_count.index)
count_traffic = list(traffic_count.id)

traffic_pie = go.Figure(data=[go.Pie(labels=types, values=count_traffic, hole=.5)])

#
geo_pie = px.sunburst(merge_df, path=['country', 'region', 'city'])

# карта трафика
traffic_map = px.scatter_mapbox(merge_df, lat='latitude', lon='longitude', hover_name='ip',
                                hover_data=['country', 'region', 'city'], zoom=config.map_zoom,
                                center=config.map_center, color='protocol', height=800)
traffic_map.update_layout(mapbox_style='open-street-map')
