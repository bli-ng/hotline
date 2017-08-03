import socket


class Session():
    '''
    Generic class for sessions to inherit from
    '''

    def __init__(self):
        pass

    def send(self, message):
        pass

    def recv(self, bytecount):
        pass


class TCPSession():

    def __init__(self, host=None, port=None, open_socket=None):
        assert((host is not None or port is not None)
               != open_socket is not None)
        if open_socket is not None:
            self.socket = open_socket
        else:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))

    def send(self, message):
        self.socket.send(message.encode('utf-8'))

    def send_binary(self, binary):
        self.socket.send(binary)

    def recv(self):
        return self.socket.recv(1024).decode('utf-8')

    def recv_exact(self, recvcount):
        return self.socket.recv(recvcount).decode('utf-8')

    def recv_binary(self):
        return self.socket.recv(1024)

    def recv_binary_exact(self, recvcount):
        return self.socket.recv(recvcount)
