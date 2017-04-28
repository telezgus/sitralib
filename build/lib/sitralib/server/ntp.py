import datetime
import socket
import struct
from socket import AF_INET, SOCK_DGRAM
from time import ctime


def getNTPTime(host="pool.ntp.org"):
    port = 123
    buf = 1024
    address = (host, port)
    msg = '\x1b' + 47 * '\0'

    # reference time (in seconds since 1900-01-01 00:00:00)
    # TIME1970 = 2208988800L # 1970-01-01 00:00:00
    TIME1970 = 2208988800  # 1970-01-01 00:00:00
    try:
        # connect to server
        client = socket.socket(AF_INET, SOCK_DGRAM)
        client.sendto(msg.encode('utf-8'), address)
        msg, address = client.recvfrom(buf)

        t = struct.unpack("!12I", msg)[10]
        t -= TIME1970

        return datetime.datetime.strptime(ctime(t), "%a %b %d %H:%M:%S %Y")
    except:
        return None


if __name__ == "__main__":
    d = getNTPTime(host="pool.ntp.org")
    # print(d)
    # print(d.day, d.month, d.year, d.hour, d.minute, d.second, d.weekday(), d.microsecond)
