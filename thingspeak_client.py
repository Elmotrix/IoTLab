import thingspeak;
from datetime import datetime
from datetime import timedelta
channel_id = 1874852;
write_key = "X84W65YDVP1FXTNM";

channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    
lastPrintTime = datetime.now() - timedelta(seconds = 15)
def ThingPrint(value1,value2):
    global lastPrintTime
    if (datetime.now() > lastPrintTime + timedelta(seconds = 15) or True):
        lastPrintTime = datetime.now()
        response = channel.update({'field1':value1,'field2':value2})
