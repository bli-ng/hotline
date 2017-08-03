import threading
import subprocess
import io
from hotline.async_buffer import AsyncBuffer


class Shell():
    '''
    Opens a shell on the system
    '''

    def __init__(self,  payload):
        threading.Thread.__init__(self)
        self.payload = payload
        self.spawn()

    def spawn(self):
        self._proc = subprocess.Popen(self.payload, shell=True,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        self._shellin = io.TextIOWrapper(
            self._proc.stdin,
            encoding='utf-8',
            line_buffering=True,  # send data on newline
        )
        self._shellout = AsyncBuffer(self._proc.stdout)
        self._shellerr = AsyncBuffer(self._proc.stderr)

    def can_read(self):
        '''Return true if output can be read'''
        return not self._shellout.empty()

    def read(self):
        '''Return the shell output'''
        if not self._shellout.empty():
            return self._shellout.read()
        return None

    def write(self, user_input):
        '''Write to the shell process'''
        self._shellin.write(user_input)

    def error(self):
        '''Return the shell error'''
        if not self._shellerr.empty():
            return self._shellerr.read()
        return None
