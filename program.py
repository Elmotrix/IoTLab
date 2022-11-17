import time;
import mqtt_client
import database
import thingspeak_client
import LowPassFilter
import sensor
import PinControll
from datetime import datetime
from datetime import timedelta

tmpFilter = LowPassFilter.Filter()
tcFilter = LowPassFilter.Filter()
alarm = False
PrintInterval = 20
alarmTemp = 28;


lastPrintTime = datetime.now() - timedelta(seconds = PrintInterval)
while True:
    sensorValueTMP = PinControll.ReadSensorTMP36()
    sensorValueTC = PinControll.ReadSensorTC74()
    filteredValueTMP = tmpFilter.FilterValue(sensorValueTMP);
    filteredValueTC = tcFilter.FilterValue(sensorValueTC);
    if (datetime.now() > lastPrintTime + timedelta(seconds = PrintInterval)):
        lastPrintTime = datetime.now()
        print("Raw SensorValue TMP36: " + str(sensorValueTMP))
        print("Filter SensorValue TMP36: " + str(filteredValueTMP))
        print("Raw SensorValue TC74: " + str(sensorValueTC))
        print("Filter SensorValue TC74: " + str(filteredValueTC))
        database.MongoPrint(filteredValueTMP);
        mqtt_client.publish(filteredValueTMP)
        thingspeak_client.ThingPrint(filteredValueTMP,filteredValueTC)
    if (sensorValueTMP >= alarmTemp or sensorValueTC >= alarmTemp):
        alarm = True
    if not PinControll.ReadButton():
        alarm = False
    PinControll.SetLed(alarm)
    time.sleep(0.1)