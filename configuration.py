import datetime
from fastapi import FastAPI, Body


app = FastAPI()

header = {
            "key": "Content-Type",
            "value": "application/json",
            "type": "text",
        }


# instant time info
dateHour= datetime.datetime.now().hour
dateMinute= datetime.datetime.now().minute
dateSecond= datetime.datetime.now().second
dateMilisecond= datetime.datetime.now().microsecond