class SessionManager():

    def __init__(self, sessions=[]):
        self.sessions = sessions
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)
        listener.pool_sessions(self.sessions)
