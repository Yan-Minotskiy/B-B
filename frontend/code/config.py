import pandas as pd
from os import environ


database = {
    'host': environ.get('POSTGRES_HOST'),
    'port': 5432,
    'database': environ.get('POSTGRES_DB'),
    'user': environ.get('POSTGRES_USER'),
    'password': environ.get('POSTGRES_PASSWORD')
}

example_for_maps = pd.DataFrame(data=
                                {'Ip адрес': ["66.254.114.41", "18.66.248.43", '34.95.71.207'],
                                 'Страна': ["Russia", "Germany", "Unated States"],
                                 'Широта': [55.7938143, 50.11, 39.09],
                                 'Долгота': [37.7013855, 8.68, -94.57],
                                 'Регион': ["Moscow", "Hesse", "Missouri"],
                                 'Город': ["Moscow", "Frankfurt", "Kansas City"]}
                                )

Moscow_lon = 37.61
Moscow_lat = 55.75
