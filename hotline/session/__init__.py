import socket
from hotline.async_buffer import AsyncBuffer


class TCPSession():

    def __init__(self, host=None, port=None, open_socket=None):
        assert((host is not None or port is not None)
               != open_socket is not None)
        if open_socket is not None:
            self.socket = open_socket
        else:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        self._buffer = AsyncBuffer(open(self.socket.fileno()))

    def __str__(self):
        return 'TCP - ' + self.socket.getpeername()

    def send(self, message):
        self.socket.send(message.encode('utf-8'))

    def send_binary(self, binary):
        self.socket.send(binary)

    def can_recv(self):
        '''Return true if output can be read'''
        return not self._buffer.empty()

    def recv(self):
        '''Return the shell output'''
        if not self._buffer.empty():
            return self._buffer.read()
        return None
