import json as jsonlib
import random, string
from typing import Union
from colorama import Fore,Style
class Utility:
    def __init__(self):
        self.config = self.getConfig()
        self.proxy = self.getProxy()
        self.username = self.getUsername()
    def getProxy(self) -> Union[str, None]:
        if self.config.get("proxy").get("proxyless"):
            return None
        return f'http://{random.choice(open("input/proxies.txt").readlines())}'
    def getConfig(self) -> dict:
        return jsonlib.loads(open("config.json").read())
    def getUsername(self) -> str:
        if self.config.get("username").get("use_username_from_file"):
            return random.choice(open('input/usernames.txt').readlines())
        return f"{self.config.get('username').get('username_prefix')} |" + "".join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
class MPrint:
    def __init__(self):
        """"""
    def w_print(self, message: str):
        """Print warning"""
        print(f"[{Style.BRIGHT}{Fore.RED}?{Style.RESET_ALL}] {Style.BRIGHT}{Fore.YELLOW}{message}{Style.RESET_ALL}")
    def s_print(self, message: str):
        """Print SUCCESS"""
        print(f"[{Style.BRIGHT}{Fore.MAGENTA}+{Style.RESET_ALL}] {Style.BRIGHT}{Fore.GREEN}{message}{Style.RESET_ALL}")
    def f_print(self, message: str):
        """Print FAIL"""
        print(f"[{Style.BRIGHT}{Fore.YELLOW}-{Style.RESET_ALL}] {Style.BRIGHT}{Fore.RED}{message}{Style.RESET_ALL}")