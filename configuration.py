import datetime
from fastapi import FastAPI, Body

requestUrl = "https://3ee7-159-146-18-161.ngrok.io"

app = FastAPI()

header = {
            "key": "Content-Type",
            "value": "application/json",
            "type": "text",
        }


# time
dateHour= datetime.datetime.now().hour
dateMinute= datetime.datetime.now().minute
dateSecond= datetime.datetime.now().second
dateMilisecond= datetime.datetime.now().microsecond