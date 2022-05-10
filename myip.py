#!/usr/bin/python3
from colorama import * 
import json
import requests

ip = requests.get('https://api.myip.com/')
dict_ = json.loads(ip.text)


print(f"{Fore.RED}IP: {Fore.GREEN}{dict_['ip']}{Style.RESET_ALL}")
print(f"{Fore.RED}COUNTRY: {Fore.GREEN}{dict_['country']}{Style.RESET_ALL}")
print(f"{Fore.RED}CC: {Fore.GREEN}{dict_['cc']}{Style.RESET_ALL}")



