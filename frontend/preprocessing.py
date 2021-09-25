import pandas as pd

def get_frame():
    return pd.read_sql("SELECT * FROM frame", conn)

def get_ip_location():
    return pd.read_sql("SELECT * FROM ip_location", conn)

def get_frame_with_source_ip_info():
    return pd.read_sql("SELECT * FROM frame" 
                       "INNER JOIN ip_location WHERE frame.s_ip=ip_location.id")