import requests
from configuration import *
from telemetryData import *
import time


def main():
    while True:
        try:
            ## Check Team Login 
            url=f"{requestUrl}/login"
            teamLoginInfo = requests.get(url=url, json=teamLogin,headers=header)
            print('\nteamLogin :',teamLoginInfo.json())

            ## Get Server Time From Server
            url=f"{requestUrl}/serverTime"
            getServerTime = requests.get(url=url, json=serverTime,headers=header)
            print('\ngetServerTime :',getServerTime.json())

            ## Send Telemtery Data To Server
            url=f"{requestUrl}/telemetryData"
            responseTelemetryData = requests.post(url=url, json=telemetryData,headers=header)
            print('\ntelemetryData :',responseTelemetryData.json())

            ## Send Tracking Data To Server
            url=f"{requestUrl}/tracking"
            tracking = requests.post(url=url, json=trackingData,headers=header)
            print('\ntracking :',tracking.json())

            ## Send Kamikaze Data To Server
            url=f"{requestUrl}/kamikazeInfo"
            kamikaze = requests.post(url=url, json=kamikazeData,headers=header)
            print('\nKAMİKAZE DATA :',kamikaze.json())

            ## Send Qr Data To Server
            url=f"{requestUrl}/qrCoordinate"
            qr = requests.post(url=url, json=qrData,headers=header)
            print('\nQR DATA :',qr.json())

            time.sleep(2) 
            
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
            print("Response content:", teamLoginInfo.content)

if __name__ == "__main__":
    main()