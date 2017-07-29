import logging
import threading

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class SessionChecker(threading.Thread):

    def __init__(self, sessions):
        super().__init__()
        self.sessions = sessions
        self.start()

    def run(self):
        while True:
            sessions_copy = self.sessions[:]
            for session in sessions_copy:
                if not session.test():
                    print(session)
                    self.sessions.remove(session)


class SessionManager():

    def __init__(self, sessions=[]):
        self.sessions = sessions
        self.listeners = []
        self.checker = SessionChecker(self.sessions)

    def add_listener(self, listener):
        self.listeners.append(listener)
        listener.pool_sessions(self.sessions)
