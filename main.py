from scapy.all import AsyncSniffer
from time import sleep
import socket
import struct


def unpack_ethernet_frame(data: bytes) -> tuple[str, str, int, bytes]:
    """
    :param data:
    :return: tuple
    returns converted
    mac addresses from bytes to string
    protocol number from bytes to int
    and the rest of the packet in bytes
    """
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_address(dest_mac), get_mac_address(src_mac), proto, data[14:]


def get_mac_address(byttes_addr: str) -> str:
    """
    :param byttes_addr: str
    :return: str
    converts mac address from hexstring to human readable string
    """
    bytes_str = map('{:02x}'.format, byttes_addr)
    return ':'.join(bytes_str).upper()


def unpack_ipv4_packet(data):
    version = data[0] >> 4
    ihl = (data[0] & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    if proto in PROTOCOLS:
        return version, ihl, ttl, PROTOCOLS[proto], get_ipv4_address(src), get_ipv4_address(target)
    else:
        return version, ihl, ttl, proto, get_ipv4_address(src), get_ipv4_address(target)


def get_ipv4_address(byttes_addr: str) -> str:
    """
    :param byttes_addr: str
    :return: str
    converts ip address from hexstring to human readable string
    """
    return '.'.join(map(str, byttes_addr))


def main():
    traffic_sniffer = AsyncSniffer()
    traffic_sniffer.start()
    count = 0
    while True:
        sleep(5)
        results = traffic_sniffer.stop()
        traffic_sniffer = AsyncSniffer()
        traffic_sniffer.start()
        for i, bytes_packet in enumerate(results.res):
            count += 1
            bytes_packet = bytes_packet.__bytes__()
            packet = {}  # Need to write a class ?
            packet['dest_mac'], packet['src_mac'], packet['eth_proto'], packet['ip_data'] = unpack_ethernet_frame(
                bytes_packet)
            packet['ip-version'], packet['ihl'], packet['ttl'], packet['proto'], packet['ip_src'], packet[
                'ip_dest'] = unpack_ipv4_packet(packet['ip_data'])
            print(str(count).zfill(5), packet['proto'], packet['src_mac'], packet['dest_mac'], packet['ip_src'],
                  packet['ip_dest'])


if __name__ == '__main__':
    PROTOCOLS = {num: name[8:] for name, num in vars(socket).items() if name.startswith('IPPROTO')}
    main()
