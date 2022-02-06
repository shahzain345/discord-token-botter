import threading
from botter import Botter
# author shahzain, github.com/shahzain345
def genToken():
    while True:
            botter = Botter("xTw8tUb9", "df4636c6450c100e9d8f75f439833cba")
            botter.generateToken()
threads = []
for i in range(200):
     t = threading.Thread(target=genToken, daemon=True)
     t.start()
     threads.append(t)
for i in range(200):
    threads[i].join()