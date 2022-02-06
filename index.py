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
threadCount = int(input("Enter thread count: "))
for i in range(threadCount):
     t = threading.Thread(target=genToken)
     t.start()
     threads.append(t)
for i in range(threadCount):
    threads[i].join()
