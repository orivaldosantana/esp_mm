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
gpio_rele1 = Pin(2, Pin.OUT)
gpio_rele1.value(1); 


intervalo_tempo_ligado = 2 # tempo em que o sinal fica em alta 
tempo_que_ligou = 0

estado_ligado = False 

#ssid = 'Bernadete_Brito'
#password = '22081961'
ssid = 'HughesNet_34E894'
password = 'HN841878'

mqtt_server = '157.230.89.7'
server_port=1883
mqtt_user='mqtt'
mqtt_password='oriva_mqtt'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'sitio/portao/rele1'
topic_pub = b'sitio/portao/vivo'

last_message = 0
message_interval = 60
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())



