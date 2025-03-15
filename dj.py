import requests
import os
import time
import sys
import webbrowser
from fake_useragent import UserAgent


E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(23.0 / 8000)

to(
    f"""{G}|{C}=============================================={G}|
{G}| Creator        : @Haxkx &  {G}         |
{G}| {Y}Tools       :  SafeUm Account Creator Updated       {G}   |
{G}| {PN}Expire     :  LIFETIME {G}          |
{G}| {W}Owner      :  @tanjiro_0503 @Haxkx |
{G}|{C}=============================================={G}|"""
)

import requests, random, requests, json, pyfiglet,sys,time, os, uuid, webbrowser

Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("Haxkx")
print(a_bSa+ab)
def slow(T): 
	for r in T + '\n' :
	    sys.stdout.write(r)
	    sys.stdout.flush()
	    time.sleep(30/2000)

slow(S_aBs+"""⌯ Welcome To Haxkx Safeum Account Creater  💘.
---------------------------------------------------
""")
webbrowser.open("https://t.me/haxkx")
from os import system,name
from ssl import CERT_NONE
from gzip import decompress
from random import choice,choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps
try:
	from websocket import create_connection
except:
	system('pip install websocket-client')
	from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []
def work():
	global failed,success,retry
	username = choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=12))
	try:
		con = create_connection("wss://193.200.173.45/Auth", header={"app": "com.safeum.android","host": None,"remoteIp": "193.200.173.45","remotePort": str(8080),"sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195","time": "2023-04-30 12:13:32","url": "wss://51.79.208.190/Auth"},sslopt={"cert_reqs": CERT_NONE})
		con.send(dumps({"action":"Register","subaction":"Desktop","locale":"en_IN","gmt":"+05","password":{"m1x":"186a16cf18f97cf12d8ff8d7fbd1830d5ad4e676a6fea4f35d66fa6a9c350e5d","m1y":"ad5cb4bfd447ce8d1157ca5cbe20cbadb8b42dfcbd5b8700e3301a3589c736a2","m2":"725ae65fd82697fd6ff53af0ffbfd0369a70d0f4232fe563b216f93a9eb9e6c7","iv":"b5f725dae0c1d93bda2f6dccac1e4703","message":"55fb16649fee1756f6b076ad24148c9e04afd57dc3d5c0193ea5ca41e42ab3a41fa79a5dc79898247788c2febf90cb116b6c499929b53374cacab3cd9af9f9e24b85a06f38120fa166da757f24f4710b"},"magicword":{"m1x":"35bb07cb293235a0c706a5485d4d18f79060a812b9b1a8c150dfff6aa58a177f","m1y":"f89a76f85cc082fce6980ba6168738f8a91b81f764f23bbbad34309031ca99a2","m2":"f491ecd37a7b3f6a217369b7527a90128916e9286376c87ae4b0b3ac75323610","iv":"7cfeb389a356e44d18b01d829667823d","message":"c8d557db31d12dcb81f389f97fcd1613"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 220733SPH","softwareversion":"1.1.0.1457","nickname":"jsowjj8292ff","os":"AND","deviceuid":"b0c55c7c17fddd4b","devicepushuid":"*ferPA67LYiQ:APA91bHgzqp9cw1KlfO7rYkyAuMSnc1kQPKvhPMVUbQUIqMPPYx6zTJ0Q4MtwiazYvfE8zMjSRB88o_Le0qWc_RgXHseS05iu6NpjdT5mNevquWOJmoq_GS0DfHCmBc3YBq5ALBw_VYT","osversion":"and_12.0.0","id":"84127522"}))
		gzip = decompress(con.recv()).decode('utf-8')
		if '"status":"Success"' in gzip:
			success+= 1
			accounts.append(username+':@Haxkx')
			with open('Haxkx.txt', 'a') as f: f.write(username + ":@Haxkx | TG : @Haxkx\n")
		else:
			failed+=1
	except: retry+=1

start = ThreadPoolExecutor(max_workers=1000)
while True:
    start.submit(work)
    print('\n\n\n'+' '*25+'Success : '+str(success)+'\n\n\n'+' '*25+'Failed : '+str(failed)+'\n\n\n'+' '*25+'ReTry : '+str(retry))
    if int(success) > int(0): print("\n Accounts :  "+"\n".join(accounts))
    system("cls" if name=="nt" else "clear")