import httpx
import random
from twocaptcha import TwoCaptcha

# 2captcha.com anti-captcha.com capmonster.cloud 2captcha.com
captchaApi = "2captcha.com"
proxies = open('proxies.txt').read().split('\n')

class Botter:
    def __init__(self, inv, capKey):
        try:
            self.session = httpx.Client(proxies=f"http://{random.choice(proxies)}", cookies={"locale": "en-US"}, headers={"Pragma": "no-cache", "Accept": "*/*", "Accept-Language": "en-US", "Connection": "keep-alive", "Content-Type": "application/json", "DNT": "1", "Host": "discord.com", "Referer": "https://discord.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "TE": "trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
                                        "X-Track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTk5OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="})
            # Note: If u are skidding this without adding sessions or proper headers ur token will get locked
            self.session.headers["X-Fingerprint"] = self.session.get(
                "https://discord.com/api/v9/experiments", timeout=30).json().get("fingerprint")
            self.session.headers["Origin"] = "https://discord.com"
            self.inv = inv
            self.capKey = capKey
        except:
            print('gay')
            self.generateToken()
    def getCapTwoCap(self):
        solver = TwoCaptcha(self.capKey)
        result = solver.hcaptcha(sitekey="4c672d35-0701-42b2-88c3-78380b0db560", url="discord.com")["code"]
        return result
    def getCap(self):
           solvedCaptcha = None
           captchaKey = self.capKey
           taskId = ""
           taskId = httpx.post(f"https://api.{captchaApi}/createTask", json={"clientKey": captchaKey, "task": {"type": "HCaptchaTaskProxyless", "websiteURL": "https://discord.com/",
                               "websiteKey": "4c672d35-0701-42b2-88c3-78380b0db560", "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}}, timeout=30).json()
           print(taskId)
           if taskId.get("errorId") > 0:
                print(f"[-] createTask - {taskId.get('errorDescription')}!")

           taskId = taskId.get("taskId")
            
           while not solvedCaptcha:
                    captchaData = httpx.post(f"https://api.{captchaApi}/getTaskResult", json={"clientKey": captchaKey, "taskId": taskId}, timeout=30).json()
                    if captchaData.get("status") == "ready":
                        solvedCaptcha = captchaData.get("solution").get("gRecaptchaResponse")
                        print(solvedCaptcha)
                        return solvedCaptcha
    def generateToken(self):
            payload = {
                "fingerprint": self.session.headers["X-Fingerprint"],
                "username": "GetThisToolOnGithub",
                "invite": self.inv,
                "gift_code_sku_id": None,
                "captcha_key": None
            }
            if captchaApi == "2captcha.com":
                payload["captcha_key"] = self.getCapTwoCap()
            else:
                payload["captcha_key"] = self.getCap()
            req = self.session.post('https://discord.com/api/v9/auth/register', json=payload)
            if req.status_code != 201:
                self.generateToken()
                print(req.json())
            else: 
                print(f'[>] Genned token {req.json()["token"]}')
                with open('tokens.txt', 'a') as fp:
                    fp.write(req.json()["token"] + "\n")