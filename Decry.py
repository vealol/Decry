import requests
import os
import colorama

from colorama import Fore, Style
from os import system


def purpleblue(text):
    system(""); faded = ""
    red = 110
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;255m{line}\033[0m\n")
        if not red == 0:
            red -= 15
            if red < 0:
                red = 0
    return faded

w = Fore.WHITE
g = Fore.GREEN

os.system('clS')
w='\033[1;37m'
r='\033[1;31m'
g='\033[1;32m'
y='\033[1;33m'

print(purpleblue("""
████████▄     ▄████████  ▄████████    ▄████████ ▄██   ▄   
███   ▀███   ███    ███ ███    ███   ███    ███ ███   ██▄ 
███    ███   ███    █▀  ███    █▀    ███    ███ ███▄▄▄███ 
███    ███  ▄███▄▄▄     ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███ 
███    ███ ▀▀███▀▀▀     ███        ▀▀███▀▀▀▀▀   ▄██   ███ 
███    ███   ███    █▄  ███    █▄  ▀███████████ ███   ███ 
███   ▄███   ███    ███ ███    ███   ███    ███ ███   ███ 
████████▀    ██████████ ████████▀    ███    ███  ▀█████▀  
                                     ███    ███ Dev worm 
md5\nsha1\nMySQL\nNTLM\nSHA256\nSHA512 
"""))
type=input(f"{Style.BRIGHT}{g}[ Hash Type: {g}]{w} ").lower()
hash=input(f"{Style.BRIGHT}{g}[ Input Hash: {g}]{w} ")
email='nnb85353@zwoho.com'
code='9c512744205f079c'

req=requests.get('https://md5decrypt.net/Api/api.php?hash='+hash+'&hash_type='+type+'&email='+email+'&code='+code)
out=(req.text)
print(f"\n{g}[ {w}Results {g}]{w} ",out)

pause = input("Enter to Exit Decry..")

if 'ERROR CODE : 001' in str(out):
	print("%sThe daily limit has been reached"%(r))
elif 'ERROR CODE : 002' in str(out):
	print("%sThere is an error in the email address/code, please contact mea"%(r))
elif 'ERROR CODE : 003' in str(out):
	print("%sHash length exceeds 400 characters"%(r))
elif 'ERROR CODE : 004' in str(out):
	print("%sThe server does not have a hash database type %s"%(r,type))
elif 'ERROR CODE : 005' in str(out):
	print("%sThe hash entered does not match the Hash Type"%(r))
elif 'ERROR CODE : 006' in str(out):
	print("%sInput cannot be empty, please check again"%(r))