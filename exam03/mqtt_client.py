import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.client as paho
import time

t = np.arange(0, 10, 0.1) # time vector; create Fs samples between 0 and 10.0 sec.
x = np.arange(0, 10, 0.01) # signal vector; create Fs samples
y = np.arange(0, 10, 0.01) # signal vector; create Fs samples
z = np.arange(0, 10, 0.01) # signal vector; create Fs samples
v = np.arange(0, 10, 0.01) # log data; create Fs samples

mqttc = paho.Client()

# Settings for connection
host = "localhost"
topic= "velocity"
port = 1883

# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    data = str(msg.payload)
    #split the data
    data = data.split()
    #x
    for i in range(0, 100):
        x[i] = float(data[i])
    # y
    for i in range(0, 100):
        y[i] = float(data[i + 100])
    # z
    for i in range(0, 100):
        z[i] = float(data[i + 200])
    # v
    for i in range(0, 100):
        v[i] = float(data[i + 300])

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")
# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

mqttc.loop_forever()