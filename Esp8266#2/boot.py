import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp

from machine import Pin

button = Pin(16, Pin.IN)
esp.osdebug(None)
import gc
gc.collect()

ssid = 'Crockett'
password = 'texpa-18'
mqtt_server = '192.168.1.85'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'hello'
topic_pub = b'notification'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())