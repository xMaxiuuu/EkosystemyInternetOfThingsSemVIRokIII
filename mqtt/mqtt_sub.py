from sense_emu import SenseHat
import paho.mqtt.client as mqtt
sense = SenseHat

mqtt_broker_address = ('0.0.0.0', 1833)
local_address = ('0.0.0.0', 4050)

client = mqtt.Client = ("sub1")
client.connect(mqtt_broker_address[0])

#colors
blue = (0,0,255)
white = (255,255,255)

def on_message(client, userdata, message):
    data = message.payload
    value = 64*int(data)/100
    pixels = [blue if i < value else white for i in range(64)]
    sense.set_pixels(pixels)

client.on_message = on_message
client.subscribe("humidity")
client.loop_start()
