# library's
import socket
import psycopg2

# configs
from config import database
# locale file import
from ipcheck import what_geo
from network_frames import Packet


def main():
    count = 0
    conn = psycopg2.connect(**database)
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    s.bind((INTERFACE, 0))
    while True:
        cur = conn.cursor()
        count += 1
        bytes_packet, addr = s.recvfrom(65535)
        packet = Packet(bytes_packet)
        if packet.src_mac == packet.dest_mac:
            continue
        if packet.src_ip != 'NULL':
            if f"'{database['host']}'" in [packet.src_ip, packet.dest_ip]:
                continue
            cur.execute(f"SELECT id FROM ip_location WHERE ip = {packet.src_ip}")
            if not cur.fetchall():
                geo = what_geo(packet.src_ip)
                if geo and geo['status'] != 'fail':
                    req = f"INSERT INTO ip_location (ip, country, country_code, latitude, longitude, region, city) VALUES ('{geo['query']}', '{geo['country']}', '{geo['countryCode']}', {geo['lat']}, '{geo['lon']}', '{geo['regionName']}', '{geo['city']}');"
                    cur.execute(req)
        req = f"INSERT INTO frame (protocol, s_mac, d_mac, s_ip, d_ip, s_port, d_port, data, arrival_time) VALUES ('{packet.proto}', '{packet.src_mac}', '{packet.dest_mac}', {packet.src_ip}, {packet.dest_ip}, {packet.src_port}, {packet.dest_port}, '{packet.data}', '{packet.arrival_time}');"
        cur.execute(req)
        conn.commit()
        cur.close()


if __name__ == '__main__':
    PROTOCOLS = {num: name[8:] for name, num in vars(socket).items() if name.startswith('IPPROTO')}
    INTERFACE = socket.if_nameindex()[1][1]
    main()
