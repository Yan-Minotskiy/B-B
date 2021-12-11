from os import environ

# настройки подключения к базе данных
database = {
    'host': environ.get('POSTGRES_HOST'),
    'port': 5432,
    'database': environ.get('POSTGRES_DB'),
    'user': environ.get('POSTGRES_USER'),
    'password': environ.get('POSTGRES_PASSWORD')
}

# настройки карт
map_zoom = 3
map_center = {
    'lon': 37.61,
    'lat': 55.75
}
