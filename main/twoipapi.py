# from twoip import TwoIP
from ipcheck import check_white_ip
import requests
import json


def what_geo(ip_address):
    if check_white_ip(ip_address):
        try:
            r = requests.request(method='get', url=f'http://ip-api.com/json/{ip_address}')
            return r.json()
        except:
            return None
