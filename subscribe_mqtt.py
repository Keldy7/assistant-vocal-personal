import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    
    if rc == 0:
        print("Connected with result code ")
        global connectedd
        connectedd = True

    else:
        print("Bad connection with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))

connectedd =  False
msgreceived = False

#broker = "10.55.39.90"
broker = "broker.hivemq.com"
port = 1883
user = ""
pswd = ""
MQTTv5 = 5

client = mqtt.Client()
client.username_pw_set(user,password=pswd)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_start()
client.subscribe("testtopic/1")

while connectedd != True and msgreceived != True:
    time.sleep(0.1)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_stop()
#client.loop_forever()