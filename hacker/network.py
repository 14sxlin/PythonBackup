import socket
import os
import sys


def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        ans = s.recv(1024)  # receive 1024B
        return ans
    except:
        return


def check_vulns(banner, filename):
    f = open(filename, "r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("Server is Vulnerale {}".format(banner.strip("\n")))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("{} not exists".format(filename))
            exit(0)
        if not os.access(filename, os.R_OK):
            print("{} access denied".format(filename))
            exit(0)

        portList = [21, 22, 25, 80, 110, 443]
        for x in range(147, 150):
            ip = "192.168.95." + str(x)
            for port in portList:
                banner = ret_banner(ip, port)
                if banner:
                    print(" {} : {}".format(ip, banner))
                    check_vulns(banner, filename)

    else:
        print("Usage : {0} <vlun filename>".format(str(sys.argv[0])))
        exit(0)


if __name__ == '__main__':
    main()
