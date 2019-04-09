# Complete project details at https://RandomNerdTutorials.com

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

from machine import Pin
#GPIO is equal to D2 
gpio_rele1 = Pin(4, Pin.OUT)
gpio_rele1.value(0); 

ssid = '****'
password = '****'
mqtt_server = 'm16.cloudmqtt.com'
server_port=000
mqtt_user='****'
mqtt_password='****'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'rele1'
topic_pub = b'hello'

last_message = 0
message_interval = 30
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

