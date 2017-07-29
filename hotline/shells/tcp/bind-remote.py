import socketserver
import time
from hotline.shells import Shell

HOST = 'localhost'
PORT = 1729
PAYLOAD = ['/bin/sh']


class BindShell(socketserver.BaseRequestHandler):

    def handle(self):
        shell = Shell(PAYLOAD)
        while True:
            self.request.sendall('> '.encode('utf8'))
            self.data = self.request.recv(1024)
            shell.write(self.data.decode('utf8'))
            time.sleep(.01)
            while shell.can_read():
                self.request.sendall(shell.read().encode('utf8'))


def main():
    server = socketserver.TCPServer((HOST, PORT), BindShell)
    server.serve_forever()

if __name__ == "__main__":
    main()
