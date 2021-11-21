import ipaddress


def valid_ip(address):
    try: 
        ipaddress.IPv4Address(address)
        return True
    except Exception:
        return False


def check_white_ip(ip_address):
    if valid_ip(ip_address):
        ip_address = ipaddress.IPv4Address(ip_address)
        grey = [
            ipaddress.ip_network('10.0.0.0/8'),
            ipaddress.ip_network('172.16.0.0/12'),
            ipaddress.ip_network('192.168.0.0/16'),
            ipaddress.ip_network('100.64.0.0/10')
        ]
        return not True in [ip_address in i for i in grey]
