import json
import Adafruit_DHT
import time
import sys

sys.path.append("/home/pi/.local/lib/python3.9/site-packages")
import paho.mqtt.client as mqtt

# Raspi seosor setup
sensor = Adafruit_DHT.DHT11
pin = 2

# mqtt protocol setup
client = mqtt.Client()
client.connect('192.168.0.11', 1883)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin);
    if humidity is not None and temperature is not None:
        client.publish('test', json.dumps({"temperature": temperature, "humidity": humidity}), 0)
        print("well published")
    else:
        print('Failed to get reading. Try again!')
        client.disconnect()
