

from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from telemetryData import teamLogin, telemetryData, serverTime,trackingData ,kamikazeData ,qrData, responseTelemetryData


app = FastAPI()

@app.get("/login")
async def root(body: dict = Body(...)):
    if body["kadi"]==teamLogin["kadi"] and body["sifre"]==teamLogin["sifre"]:
        login = 'Login Successfully'
        print(body)
        
        return login
    else:
        message = 'Access Denied. Please check your login information.'
        return message

@app.post("/telemetryData")
async def root(body: dict = Body(...)):
    if body:
        telemetry = f"Received telemetryData :  {responseTelemetryData}"
        print(body)
        
        return telemetry
    else:
        message = 'Missing Data'
        return message

@app.get("/serverTime")
async def root(body: dict = Body(...)):
    if body:
        serverTime = 'Received serverTime'
        print(body)
        
        return serverTime
    else:
        message = 'Missing Data'
        return message
    
    
@app.post("/tracking")
async def root(body: dict = Body(...)):
    if body:
        tracking = 'Received tracking Info'
        print(body)
        return tracking
    else:
        message = 'Missing Data'
        return message
    
    
@app.post("/kamikazeInfo")
async def root(body: dict = Body(...)):
    if body:
        kamikaze = 'Received kamikazeInfo'
        print(body)
        return kamikaze
    else:
        message = 'Missing Data'
        return message
    
@app.post("/qrCoordinate")
async def root(body: dict = Body(...)):
    if body:
        qr = 'Received qrCoordinate'
        print(body)
        return qr
    else:
        message = 'Missing Data'
        return message