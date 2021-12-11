# library's
import socket
from os import environ
from psycopg2 import connect
import netifaces as ni

# configs
from config import database
# locale file import
from ipcheck import what_geo, check_white_ip
from network_frames import Packet


def check_ip_in_database(cur, ip):
    if check_white_ip(ip):
        cur.execute('SELECT id FROM ip_location WHERE ip=%s', (ip,))
        return not cur.fetchall()
    return False


def insert_into_ip_location(cur, geo):
    req = 'INSERT INTO ip_location (ip, country, country_code, latitude, longitude, region, city) ' \
          'VALUES (%s, %s, %s, %s, %s, %s, %s);'
    params = (
        str(geo['query']),
        str(geo['country']),
        str(geo['countryCode']),
        float(geo['lat']),
        float(geo['lon']),
        str(geo['regionName']),
        str(geo['city'])
    )
    cur.execute(req, params)


def insert_into_frame(cur, packet):
    if packet.src_ip == HOST_IP:
        type = 'Исходящий'
    elif packet.dest_ip == HOST_IP:
        type = 'Входящий'
    else:
        type = 'Транзитный'
    req = 'INSERT INTO frame (type, arrival_time, protocol, s_mac, d_mac'
    params = [type, str(packet.arrival_time), str(packet.proto), str(packet.src_mac), str(packet.dest_mac)]
    if packet.src_ip:
        req += ', s_ip'
        params.append(str(packet.src_ip))
    if packet.dest_ip:
        req += ', d_ip'
        params.append(str(packet.dest_ip))
    if packet.src_port:
        req += ', s_port'
        params.append(int(packet.src_port))
    if packet.dest_port:
        req += ', d_port'
        params.append(int(packet.dest_port))
    if packet.data:
        req += ', data'
        params.append(str(packet.data))
    req += ') VALUES (%s' + ', %s' * (len(params) - 1) + ');'
    cur.execute(req, params)


def main():
    conn = connect(**database)
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    s.bind((INTERFACE, 0))
    while True:
        cur = conn.cursor()
        bytes_packet, addr = s.recvfrom(65535)
        packet = Packet(bytes_packet)
        if packet.src_mac == packet.dest_mac:
            continue
        if packet.src_ip == API_IP or packet.dest_ip == API_IP:
            continue
        if packet.src_ip:
            if database['host'] in [packet.src_ip, packet.dest_ip]:
                continue
            if check_ip_in_database(cur, packet.src_ip):
                geo = what_geo(packet.src_ip)
                if geo and geo['status'] != 'fail':
                    insert_into_ip_location(cur, geo)

            if check_ip_in_database(cur, packet.dest_ip):
                geo = what_geo(packet.dest_ip)
                if geo and geo['status'] != 'fail':
                    insert_into_ip_location(cur, geo)

        insert_into_frame(cur, packet)
        conn.commit()
        cur.close()


if __name__ == '__main__':
    PROTOCOLS = {num: name[8:] for name, num in vars(socket).items() if name.startswith('IPPROTO')}
    INTERFACE = environ.get('INTERFACE')
    API_IP = socket.gethostbyname('ip-api.com')
    if not INTERFACE:
        INTERFACE = socket.if_nameindex()[1][1]
    HOST_IP = ni.ifaddresses(INTERFACE)[ni.AF_INET][0]['addr']
    main()
