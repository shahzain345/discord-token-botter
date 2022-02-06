import threading
import os
import pyfiglet
from colorama import Fore, Style
from botter import Botter
import json
# author shahzain, github.com/shahzain345
with open('config.json') as fp:
    config = json.load(fp)
def genToken(inv):
    while True:
            botter = Botter(inv, config["capKey"])
            botter.generateToken()
os.system('cls')
os.system('title Discord-Botter')
print(pyfiglet.figlet_format("Discord Botter"))
print(f'{Style.BRIGHT}By Shahzain')
with open("proxies.txt") as fp:
    proxs = fp.read().splitlines()
if len(proxs) == 0:
    print(f'{Fore.RED}{Style.BRIGHT}Please input some proxies {Style.RESET_ALL}')
    input('Press enter to exit: ')
    exit()
threadCount = int(input(f"{Fore.GREEN}{Style.BRIGHT}[>] Enter thread count: {Style.RESET_ALL}"))
invite = str(input(f"{Fore.GREEN}{Style.BRIGHT}[>] Enter Server Invite Code: {Style.RESET_ALL}"))
threads = []
for i in range(threadCount):
     t = threading.Thread(target=genToken, args=(invite, ))
     t.start()
     threads.append(t)
for i in range(threadCount):
    threads[i].join()
