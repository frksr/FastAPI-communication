

from telemetryData import *
from configuration import *



# incoming team info
@app.get("/login")
async def root(body: dict = Body(...)):
    if body["kadi"]==teamLogin["kadi"] and body["sifre"]==teamLogin["sifre"]:
        login = 'Login Successfully'
        print(body)
        return login
    else:
        message = 'Access Denied. Please check your login information.'
        return message


# incoming server time 
@app.get("/serverTime")
async def root(body: dict = Body(...)):
    if body:
        serverTime = 'Received serverTime'
        return serverTime
    else:
        message = 'Missing Data'
        return message


# incoming telemetry info
@app.post("/telemetryData")
async def root(body: dict = Body(...)):
    if body:
        # response 
        telemetry = f"Received telemetryData :  {responseTelemetryData}"
        print(body)
        return telemetry
    else:
        message = 'Missing Data'
        return message

    
# incoming tracking info
@app.post("/tracking")
async def root(body: dict = Body(...)):
    if body:
        tracking = 'Received tracking Info'
        return tracking
    else:
        message = 'Missing Data'
        return message
    
# incoming kamikaze info
@app.post("/kamikazeInfo")
async def root(body: dict = Body(...)):
    if body:
        kamikaze = 'Received kamikazeInfo'
        return kamikaze
    else:
        message = 'Missing Data'
        return message
    
# incoming qr coordinate
@app.post("/qrCoordinate")
async def root(body: dict = Body(...)):
    if body:
        qr = 'Received qrCoordinate'
        return qr
    else:
        message = 'Missing Data'
        return message