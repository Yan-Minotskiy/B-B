import config
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
analyzed = frame.shape[0] #проанализировано
input_traffic = 0 #TODO: вычислить
output_traffic = 0 #TODO: вычислить

#информация о протоколах подключения
proto_count = frame.groupby('protocol').count()

protocols = list(proto_count.index)
count_protocols = list(proto_count.id)

# Use `hole` to create a donut-like pie chart
proto_pie = go.Figure(data=[go.Pie(labels=protocols, values=count_protocols, hole=.8)])





"""
fig_map = px.scatter_mapbox(config.example_for_maps, lat="Широта", lon="Долгота", hover_name="Ip адрес",
                            hover_data=["Страна", "Регион", "Город"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=700,
                            center=dict(lon=config.Moscow_lon, lat=config.Moscow_lat))
fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r": 40, "t": 40, "l": 40, "b": 40})

# диаграмма трафика по странам
lst1 = list(set(config.example_for_maps["Страна"]))
lst2 = ["" for i in range(len(lst1))]
lst1.extend(list(config.example_for_maps["Регион"]))
lst2.extend(list(config.example_for_maps["Страна"]))
pie_country = go.Figure(go.Sunburst(
    labels=lst1,
    parents=lst2,
    values=[2, 1, 1, 1, 1],
))
pie_country.update_layout(margin=dict(t=0, l=0, r=0, b=0))
"""