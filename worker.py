import requests
from configuration import *
from telemetryData import *


## Check Team Login 

url="https://110a-159-146-14-104.ngrok.io/login"
teamLogin = requests.get(url=url, json=teamLogin,headers=header)
print('\nteamLogin :\n',teamLogin.json())


## Get Server Time From Server

url="https://110a-159-146-14-104.ngrok.io/serverTime"
getServerTime = requests.get(url=url, json=serverTime,headers=header)
print('\ngetServerTime :\n',getServerTime.json())


## Send Telemtery Data To Server

url="https://110a-159-146-14-104.ngrok.io/telemetryData"
telemetryData = requests.post(url=url, json=telemetryData,headers=header)
print('\ntelemetryData :\n',telemetryData.json())


## Send Tracking Data To Server

url="https://110a-159-146-14-104.ngrok.io/tracking"
tracking = requests.post(url=url, json=trackingData,headers=header)
print('\ntracking :\n',tracking.json())


## Send Kamikaze Data To Server

url="https://110a-159-146-14-104.ngrok.io/kamikazeInfo"
kamikaze = requests.post(url=url, json=kamikazeData,headers=header)
print('\nKAMİKAZE DATA :\n',kamikaze.json())


## Send Qr Data To Server

url="https://110a-159-146-14-104.ngrok.io/qrCoordinate"
qr = requests.post(url=url, json=qrData,headers=header)
print('\nQR DATA :\n',qr.json())