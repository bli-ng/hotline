import threading
import queue


class AsyncBuffer(threading.Thread):
    '''
    Buffers output for blocking reads
    '''

    def __init__(self, infile):
        threading.Thread.__init__(self)
        self._infile = infile
        self._queue = queue.Queue()
        self.start()

    def run(self):
        for line in self._infile:
            try:
                self._queue.put(line.decode('utf-8'))
            except AttributeError:
                self._queue.put(line)

    def empty(self):
        return not self.is_alive() or self._queue.empty()

    def read(self):
        return self._queue.get()
