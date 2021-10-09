import ipaddress


def valid_ip(address):
    try: 
        ipaddress.IPv4Address(address)
        return True
    except:
        return False


def check_white_ip(ip_addres):
    if  valid_ip(ip_addres):
        ip_addres = ipaddress.IPv4Address(ip_addres)
        grey = [
            ipaddress.ip_network('10.0.0.0/8'),
            ipaddress.ip_network('172.16.0.0/12'),
            ipaddress.ip_network('192.168.0.0/16'),
            ipaddress.ip_network('100.64.0.0/10')
        ]
        return not True in [ip_addres in i for i in grey]
