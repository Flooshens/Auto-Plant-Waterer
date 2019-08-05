# Followed this guide to get started: https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
# using umqttsimple for the MQTT micropython library. It needs umqttsimple.py downloaded from the above tutorial and placed in main folder
# with boot.py and main.py

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'Crockett'
password = '******'
mqtt_server = '192.168.1.85'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

