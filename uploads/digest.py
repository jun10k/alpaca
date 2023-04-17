import threading
from time import sleep
from .models import Document


class DigestThread(threading.Thread):
    def __init__(self, document):
        self.document = document
        super(DigestThread, self).__init__()

    def run(self):
        self.document.digest()


class DigestThreadPool:
    def __init__(self, max_threads=5):
        self.max_threads = max_threads
        self.threads = []

    def add(self, document):
        if len(self.threads) >= self.max_threads:
            for t in self.threads:
                if not t.is_alive():
                    self.threads.remove(t)
        else:
            thread = DigestThread(document)
            self.threads.append(thread)
            thread.start()

    def start(self):
        while True:
            docs = Document.objects.filter(is_processed=False)
            for doc in docs:
                self.add(doc)
                sleep(10)
            else:
                sleep(60)
