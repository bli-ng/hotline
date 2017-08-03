from hotline import SessionManager
from hotline.listener import TCPListener
import time

hotline = SessionManager()
hotline.add_listener(TCPListener('127.0.0.1', 1730))

while True:
    print(hotline.sessions)
    for session in hotline.sessions:
        session.send('whoami')
        print(session.recv())
        time.sleep(1)
    time.sleep(1)
