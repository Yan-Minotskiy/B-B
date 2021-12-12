import struct
from datetime import datetime


def get_mac_address(byttes_addr: str) -> str:
    """
    :param byttes_addr: str
    :return: str
    converts mac address from hexstring to human readable string
    returns MAC as string from bytes (like AA:BB:CC:DD:EE:FF)
    """
    bytes_str = map('{:02x}'.format, byttes_addr)
    return ':'.join(bytes_str).upper()


class Ethernet:
    def __init__(self, data: bytes):
        dest, src, prototype = struct.unpack('! 6s 6s H', data[:14])
        self.dest_mac = get_mac_address(dest)
        self.src_mac = get_mac_address(src)
        self.proto = prototype
        self.data = data[14:]


class IPv4:
    def __init__(self, data: bytes):
        self.version = data[0] >> 4
        self.ihl = (data[0] & 15) * 4
        self.ttl, self.proto, src, dest = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
        self.src = self.get_ipv4_address(src)
        self.dest = self.get_ipv4_address(dest)
        self.data = data[self.ihl:]

    @staticmethod
    def get_ipv4_address(bytes_address: str) -> str:
        """
        :param bytes_address: str
        :return: str
        converts ip address from hexstring to human readable string
        """
        return '.'.join(map(str, bytes_address))


class TCP:
    def __init__(self, data: bytes):
        (self.src_port, self.dest_port, self.sequence, self.acknowledgment, offset_reserved_flags) = struct.unpack(
            '! H H L L H', data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        self.flag_urg = (offset_reserved_flags & 32) >> 5
        self.flag_ack = (offset_reserved_flags & 16) >> 4
        self.flag_psh = (offset_reserved_flags & 8) >> 3
        self.flag_rst = (offset_reserved_flags & 4) >> 2
        self.flag_syn = (offset_reserved_flags & 2) >> 1
        self.flag_fin = offset_reserved_flags & 1
        self.data = data[offset:]


class UDP:
    def __init__(self, data: bytes):
        self.src_port, self.dest_port, self.size = struct.unpack('! H H 2x H', data[:8])
        self.data = data[8:]


class ICMP:
    def __init__(self, data: bytes):
        self.type, self.code, self.checksum = struct.unpack('! B B H', data[:4])
        self.data = data[4:]


class Packet:
    def __init__(self, bytes_packet):
        ethernet = Ethernet(bytes_packet)
        self.proto = ethernet.proto
        self.dest_mac = ethernet.dest_mac
        self.src_mac = ethernet.src_mac
        self.src_ip = None
        self.dest_ip = None
        self.src_port = None
        self.dest_port = None
        self.data = ethernet.data
        self.arrival_time = datetime.now()
        if ethernet.proto == 2048:
            ipv4 = IPv4(ethernet.data)
            self.proto = ipv4.proto
            self.src_ip = ipv4.src
            self.dest_ip = ipv4.dest
            # ICMP
            if ipv4.proto == 1:
                icmp = ICMP(ipv4.data)
                self.proto = 'icmp'
                self.data = icmp.data
            # TCP
            elif ipv4.proto == 6:
                tcp = TCP(ipv4.data)
                self.proto = 'tcp'
                self.src_port = tcp.src_port
                self.dest_port = tcp.dest_port
                self.data = tcp.data
            # UDP
            elif ipv4.proto == 17:
                udp = UDP(ipv4.data)
                self.proto = 'udp'
                self.src_port = udp.src_port
                self.dest_port = udp.dest_port
                self.data = udp.data
            if self.src_port == 80 or self.dest_port == 80:
                self.proto = 'http'
            elif self.src_port == 443 or self.dest_port == 443:
                self.proto = 'https'
            elif self.src_port == 53 or self.dest_port == 53:
                self.proto = 'dns'
            elif self.src_port == 23 or self.dest_port == 23:
                self.proto = 'telnet'
            elif self.src_port == 22 or self.dest_port == 22:
                self.proto = 'ssh'
            elif self.src_port == 21 or self.dest_port == 21:
                self.proto = 'ftp'
            elif self.src_port == 25 or self.dest_port == 25:
                self.proto = 'smtp'

        if self.proto == 2054:
            self.proto = 'ARP'
        elif self.proto == 34525:
            self.proto = 'ipv6'

        if type(self.proto) == int:
            self.proto = hex(self.proto)
        self.data = self.data.hex(':')
