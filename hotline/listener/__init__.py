import threading
import socket
import logging
from hotline.session import TCPSession


class Listener(threading.Thread):
    '''
    Generic class for listeners to inherit from
    '''

    def __init__(self, sessions=[]):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.sessions = sessions

    def pool_sessions(self, sessions):
        sessions.extend(self.sessions)
        self.sessions = sessions


class TCPListener(Listener):

    def __init__(self, bind, port, sessions=[]):
        '''
        Set up listener
        '''
        super().__init__(sessions)
        self.bind = bind
        self.port = port
        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM)
        self.socket.bind((self.bind, self.port))
        self.socket.listen(5)
        self.logger.info('Started listener: {0}:{1}'.format(self.bind,
                                                            self.port))
        self.start()

    def run(self):
        while True:
            new_socket = self.socket.accept()
            self.logger.info('{0} connected'.format(new_socket[1][0]))
            new_session = TCPSession(open_socket=new_socket[0])
            self.sessions.append(new_session)
