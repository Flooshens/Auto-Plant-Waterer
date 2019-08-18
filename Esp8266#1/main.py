# Complete project details at https://RandomNerdTutorials.com
import machine
led = machine.Pin(4, machine.Pin.OUT)

######################


rtc = machine.RTC() # Clock for deepsleep
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
#adc = machine.ADC(0) # Pin to Read sensor voltage

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
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
#  print('1')
except OSError as e:
  restart_and_reconnect()

while True:
  try:

    client.check_msg()
#    if (time.time() - last_message) > message_interval:
    msg = b'check sweetness' #% counter
    client.publish(topic_pub, msg)
    last_message = time.time()
    #counter += 1
    time.sleep(5)

  except OSError as e:
    restart_and_reconnect()
############
