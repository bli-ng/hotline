from hotline import SessionManager
from hotline.listener import TCPListener
import time

hotline = SessionManager()
hotline.add_listener(TCPListener('127.0.0.1', 1729))

while True:
    print(hotline.sessions)
    for session in hotline.sessions:
        session.send(bytes('Test\n', encoding='utf-8'))
    time.sleep(1)
