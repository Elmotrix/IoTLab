import board
import digitalio
import busio
import time;
from gpiozero import MCP3002
import smbus
channel = 1
address = 0x48
bus = smbus.SMBus(channel)

led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

adc = MCP3002(channel=0, differential=False)

def ReadButton():
    return button.value

def SetLed(state):
    led.value = state

def ReadSensorTMP36():
    return adc.value*500-50

def ReadSensorTC74():
    return float(bus.read_byte_data(address, 0))

#sudo i2cdetect -y 1
#sudo i2cget -y 1 0x48
if __name__ == '__main__':
    for i in range(50):
        print(ReadSensorTMP36())
        time.sleep(1)