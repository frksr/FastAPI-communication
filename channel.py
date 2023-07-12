

from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from telemetryData import teamLogin, telemetriData, serverTime,trackingData ,kamikazeData ,qrData 


app = FastAPI()

@app.get("/login")
async def root(body: dict = Body(...)):
    if body["kadi"]==teamLogin["kadi"] and body["sifre"]==teamLogin["sifre"]:
        message = 'Login Successfully'
        print(body)
        
        return message
    else:
        message = 'Access Denied. Please check your login information.'
        return message

@app.post("/telemetryData")
async def root(body: dict = Body(...)):
    if body:
        message = 'Received Data'
        print(body)
        
        return message
    else:
        message = 'Missing Data'
        return message

@app.get("/sunucusaati")
async def root(body: dict = Body(...)):
    if body:
        message = 'Received Data'
        print(body)
        
        return message
    else:
        message = 'Missing Data'
        return message
    
    
@app.post("/kilitlenme_bilgisi")
async def root(body: dict = Body(...)):
    if body:
        message = 'Received Data'
        print(body)
        return message
    else:
        message = 'Missing Data'
        return message
    
    
@app.post("/kamikaze_bilgisi")
async def root(body: dict = Body(...)):
    if body:
        message = 'Received Data'
        print(body)
        return message
    else:
        message = 'Missing Data'
        return message
    
@app.post("/qr_koordinati")
async def root(body: dict = Body(...)):
    if body:
        message = 'Received Data'
        print(body)
        return message
    else:
        message = 'Missing Data'
        return message