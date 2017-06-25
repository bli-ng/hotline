import threading
import subprocess
import queue
import io
import time


class LocalShellBuffer(threading.Thread):
    '''
    Buffers output for LocalShell
    '''

    def __init__(self, infile):
        threading.Thread.__init__(self)
        self._infile = infile
        self._queue = queue.Queue()
        self.start()

    def run(self):
        for line in self._infile:
            self._queue.put(line.decode('utf-8'))

    def empty(self):
        return not self.is_alive() or self._queue.empty()

    def read(self):
        return self._queue.get()


class LocalShell(threading.Thread):
    '''
    Opens a shell on the system
    '''

    def __init__(self,  payload, infile, outfile, errfile):
        threading.Thread.__init__(self)
        self.payload = payload
        self._infile = infile
        self._outfile = outfile
        self._errfile = errfile
        self.spawn()
        self.start()

    def spawn(self):
        self._proc = subprocess.Popen(self.payload, shell=True,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        self._shellout = LocalShellBuffer(self._proc.stdout)
        self._shellerr = LocalShellBuffer(self._proc.stderr)
        self._shellin = io.TextIOWrapper(
            self._proc.stdin,
            encoding='utf-8',
            line_buffering=True,  # send data on newline
        )

    def run(self):
        while True:
            if not self._shellout.empty():
                self._outfile.write(self._shellout.read())
                self._outfile.flush()
            elif not self._shellerr.empty():
                self._errfile.write(self._shellerr.read())
                self._errfile.flush()
            else:
                self._outfile.write('> ')
                self._outfile.flush()
                user_input = self._infile.readline()
                try:
                    self._shellin.write(user_input)
                    time.sleep(.01)
                except BrokenPipeError:
                    self._outfile.write('Connection closed\n')
                    self._outfile.flush()
                    exit()
