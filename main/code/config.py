from os import environ


database = {
    'host': environ.get('POSTGRES_HOST'),
    'port': 5432,
    'database': environ.get('POSTGRES_DB'),
    'user': environ.get('POSTGRES_USER'),
    'password': environ.get('POSTGRES_PASSWORD')
}
