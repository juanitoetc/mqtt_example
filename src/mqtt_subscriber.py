import paho.mqtt.client as mqtt
from random import randrange, uniform
from time import sleep

# Broker info
# Broker = "mqtt.eclipseprojects.io"
Broker = "public.mqtthq.com"
TCPPort = 1883
WebSocketPort = 8083
WebSocketPath ="/mqtt"

# MQTT Topic info
Topic = "mqtt-topic-1"
QoS = 0


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        # we should always subscribe from on_connect callback to be sure
        # our subscribed is persisted across reconnections.
        print("Connected successfully to: {}".format(Broker))
        client.subscribe(Topic)
    else:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
        raise Exception


def on_message(client, userdata, msg):
    print(msg.topic + ": " + str(msg.payload.decode("utf-8")))


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    print("Subscribed to Topic: {}.".format(Topic))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

# This will trigger the on_connect method
client.connect(Broker)
sleep(2)
client.loop_forever()


