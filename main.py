from concurrent.futures import ThreadPoolExecutor
from src import Botter, utility
from colorama import Fore,Style
from traceback import format_exc
import os
console = utility.MPrint()
def main(rawInvite: str):
    while True:
        try:
            botter = Botter(rawInvite)
            token = botter.generateToken()
            if token != None:
                open("tokens.txt", "a").write(token + "\n")
        except Exception as e:
            console.f_print(f"Unhandled Error: {e}")
            continue

if __name__ == "__main__":
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("""
███████╗██╗  ██╗ █████╗ ██╗  ██╗███████╗ █████╗ ██╗███╗   ██╗    ██████╗  ██████╗ ████████╗████████╗███████╗██████╗ 
██╔════╝██║  ██║██╔══██╗██║  ██║╚══███╔╝██╔══██╗██║████╗  ██║    ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
███████╗███████║███████║███████║  ███╔╝ ███████║██║██╔██╗ ██║    ██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔╝
╚════██║██╔══██║██╔══██║██╔══██║ ███╔╝  ██╔══██║██║██║╚██╗██║    ██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗
███████║██║  ██║██║  ██║██║  ██║███████╗██║  ██║██║██║ ╚████║    ██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
    """.replace("█", f"{Fore.BLUE}{Style.BRIGHT}█{Style.RESET_ALL}"))
    threadCount = int(input(f"[{Style.BRIGHT}{Fore.MAGENTA}+{Style.RESET_ALL}] {Style.BRIGHT}Enter your thread count: {Style.RESET_ALL}"))
    rawInvite = input(f"[{Style.BRIGHT}{Fore.MAGENTA}+{Style.RESET_ALL}] {Style.BRIGHT}Enter your invite(without discord.gg/): {Style.RESET_ALL}")
    with ThreadPoolExecutor(max_workers=threadCount) as executor:
        for _ in range(threadCount):
            executor.submit(main, rawInvite)