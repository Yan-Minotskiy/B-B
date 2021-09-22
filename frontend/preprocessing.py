import pandas as pd

def get_frame():
    return pd.read_sql("SELECT * FROM frame", conn)

def get_ip_location():
    return pd.read_sql("SELECT * FROM ip_location", conn)