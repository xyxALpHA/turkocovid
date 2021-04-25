from time import sleep
import time
import requests
import sys
import os
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("figlet TURKOCOVİD")

print ("yapimci  : xyxALpHA")
print ("website : https://www.turkhackteam.org")
print ("instagram :xyxALpHA_tht")
print ("xyxalpha.turkhackteam@yandex.com")
print("----------------------------------------")
print ("TURKOCOVİD")

print("------------------00------------------------")



chat = int(input("CHAT İD :"))
url = input("API URL :")
print("[=======sleep(1) : 1 saniye/seconds]==========")
loop = int(input("LOOP HOURS :"))
sleep(2)
print ("[==========gonderildi==========] 100%")
print ("[=========={}/s/m/h yenilenecek==========].....".format(loop))

print("EXİT : ctrl+c")


os.system("figlet TURKIYE")


while True:

 
 saat = time.localtime
 adres = "https://pomber.github.io/covid19/timeseries.json"
 durum = requests.get(adres)
 jsoncevir = durum.json()
 kacgun = len(jsoncevir["Turkey"])
 turkey = jsoncevir["Turkey"][kacgun-1]
#print(turkey)

 tarih = turkey["date"]
 vaka = turkey["confirmed"]
 olum = turkey["deaths"]
 iyilesme = turkey["recovered"]

 mesaj = "{} tarihli turkiye covid19 bilgileri asagidaki gibidir\nvaka sayisi :{}\nolum sayisi :{}\n iyilesme sayisi :{}\n saglikli gunler dileriz".format(tarih,vaka,olum,iyilesme)


 requests.post

 requests.post(url= url, data={'chat_id':chat, 'text':mesaj}).json()
 
 sleep(loop)
  