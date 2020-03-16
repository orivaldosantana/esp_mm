# Complete project details at https://RandomNerdTutorials.com

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'sitio/portao/rele1' and msg == b'v':
    print('ESP received, rele1 to on')
    gpio_rele1.value(1)
    tempo_que_ligou = time.time()
    estado_ligado = True 
  if topic == b'sitio/portao/rele1' and msg == b'f':
    print('ESP received, rele1 to off')
    gpio_rele1.value(0) 
    estado_ligado = False    

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub, server_port, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, server_port, mqtt_user, mqtt_password)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if ((time.time() - tempo_que_ligou) > intervalo_tempo_ligado ) and estado_ligado
      estado_ligado = False
      gpio_rele1.value(0)   

    if (time.time() - last_message) > message_interval:
      # write on 'Hello' topic 
      msg = b'Tempo #%d' % counter
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()


