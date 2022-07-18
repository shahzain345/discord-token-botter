from concurrent.futures import ThreadPoolExecutor
from src import Botter, utility, captcha
try:
    from colorama import Fore, Style
    import os, httpx
except:
    import os
    os.system("pip install httpx colorama twocaptcha-python")
    print("File had import errors, please restart it")
    exit()

try:
    utils = utility.Utility()
except:
    pass
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
    if (
        not os.path.exists("./config.json")
        or not os.path.exists("./input")
        or not os.path.exists("./input/proxies.txt")
        or not os.path.exists("./input/usernames.txt")
    ):
        console.f_print(
            "Couldn't start up, one of these files is missing, ./config.json, ./input/proxies.txt, ./usernames.txt"
        )
        console.s_print("Do you wish to install the missing files?(y/n)")
        resp = input("")

        if resp == "y":
            client = httpx.Client()
            if not os.path.exists("./config.json"):
                console.s_print("Config.json is missing, installing")
                try:
                    clientresp = client.get(
                        "https://raw.githubusercontent.com/shahzain345/discord-token-botter/main/config.json"
                    ).text
                    open("./config.json", "w").write(clientresp)
                except Exception as e:
                    console.f_print(f"Failed to install config.json {e}")
            if not os.path.exists("./input"):
                console.s_print("The whole input folder is missing, creating...")
                os.mkdir("./input")
                open("./input/proxies.txt", "w").write(
                    "ur proxies, username:pass@ip:port or ip:port"
                )
                open("./input/usernames.txt", "w").write("")
            os.system("cls") if os.name == "nt" else os.system("clear")
        else:
            console.f_print("Exiting...")
            exit()
    captcha = captcha.Captcha()
    print(
        """
███████╗██╗  ██╗ █████╗ ██╗  ██╗███████╗ █████╗ ██╗███╗   ██╗    ██████╗  ██████╗ ████████╗████████╗███████╗██████╗ 
██╔════╝██║  ██║██╔══██╗██║  ██║╚══███╔╝██╔══██╗██║████╗  ██║    ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
███████╗███████║███████║███████║  ███╔╝ ███████║██║██╔██╗ ██║    ██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔╝
╚════██║██╔══██║██╔══██║██╔══██║ ███╔╝  ██╔══██║██║██║╚██╗██║    ██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗
███████║██║  ██║██║  ██║██║  ██║███████╗██║  ██║██║██║ ╚████║    ██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
    """.replace(
            "█", f"{Fore.BLUE}{Style.BRIGHT}█{Style.RESET_ALL}"
        )
    )
    console.s_print(
        f"Total Proxies: {len(open('input/proxies.txt').readlines())} || Captcha Balance: ${captcha.getBalance()}"
    )
    threadCount = int(
        input(
            f"[{Style.BRIGHT}{Fore.MAGENTA}+{Style.RESET_ALL}] {Style.BRIGHT}Enter your thread count: {Style.RESET_ALL}"
        )
    )
    rawInvite = input(
        f"[{Style.BRIGHT}{Fore.MAGENTA}+{Style.RESET_ALL}] {Style.BRIGHT}Enter your invite(without discord.gg/): {Style.RESET_ALL}"
    )
    with ThreadPoolExecutor(max_workers=threadCount) as executor:
        for _ in range(threadCount):
            executor.submit(main, rawInvite)
