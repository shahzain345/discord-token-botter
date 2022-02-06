import threading
from botter import Botter
import json
# author shahzain, github.com/shahzain345
with open('config.json') as fp:
    config = json.load(fp)
def genToken():
    while True:
            botter = Botter(config["inv"], config["capKey"])
            botter.generateToken()
threads = []
for i in range(200):
     t = threading.Thread(target=genToken, daemon=True)
     t.start()
     threads.append(t)
for i in range(200):
    threads[i].join()
