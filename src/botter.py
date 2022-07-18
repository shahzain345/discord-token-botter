# Importing shit
import httpx
import os
import json as jsonlib
from base64 import b64encode
from typing import Union
from .utility import Utility, MPrint
from .captcha import Captcha

success = 0
errors = 0
console = MPrint()


class Botter(httpx.Client):
    def __init__(self, rawInvite: str):
        self.utils = Utility()
        self.captcha = Captcha()
        super().__init__(
            headers={
                "Host": "discord.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "X-Super-Properties": self.__build_trackers(),
                "X-Context-Properties": "eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9",
                "X-Discord-Locale": "en-US",
                "X-Debug-Options": "bugReporterEnabled",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": f"https://discord.com/invite/{rawInvite}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            proxies=self.utils.proxy,
            timeout=60,
        )
        self.rawInvite = rawInvite
        self.get("https://discord.com")  # Get cookies
        self.headers["X-Fingerprint"] = (
            self.get("https://discord.com/api/v9/experiments").json().get("fingerprint")
        )
        del self.headers["X-Context-Properties"]
        self.headers["Origin"] = "https://discord.com"

    def __build_trackers(self):
        return b64encode(
            jsonlib.dumps(
                {
                    "os": "Windows",
                    "browser": "Firefox",
                    "device": "",
                    "system_locale": "en-US",
                    "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
                    "browser_version": "103.0",
                    "os_version": "10",
                    "referrer": "",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 133852,
                    "client_event_source": None,
                },
                separators=(",", ":"),
            ).encode()
        ).decode()

    def _make_account(self, payload: dict, captcha: Union[str, None] = None) -> dict:
        if captcha != None:
            payload["captcha_key"] = captcha
        return self.post(
            "https://discord.com/api/v9/auth/register", json=payload
        ).json()

    def generateToken(self):
        global success
        global errors
        global timestart
        try:
            os.system(
                f"title Shahzain Botter ^| Success: {success} ^| Proxies: {len(open('input/proxies.txt').readlines())} ^| Captcha Balance: ${self.captcha.getBalance()} ^| Errors: {errors}"
            ) if os.name == "nt" else None
            payload = {
                "fingerprint": self.headers.get("X-Fingerprint"),
                "username": self.utils.username,
                "invite": self.rawInvite,
                "consent": True,
                "gift_code_sku_id": None,
                "captcha_key": None,
            }
            res = self._make_account(payload)
            if "captcha_key" in res:
                res = self._make_account(payload, self.captcha.getCaptcha())
            if "token" in res:
                success += 1
                console.s_print(
                    f"Generated {res.get('token')} || {payload.get('username')}"
                )
                return res.get("token")
            if "token" not in res:
                console.f_print(f"Failed token not in variable 'res': {res}")
                errors += 1
                return None
        except Exception as e:
            console.f_print(f"Error: {e}")
            errors += 1
            return None
