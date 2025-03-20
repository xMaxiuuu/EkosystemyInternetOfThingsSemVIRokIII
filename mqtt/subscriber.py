# SUBSCRIBER
from sense_emu import SenseHat
import paho.mqtt.client as mqtt

sense = SenseHat()

mqtt_broker_address = "localhost"
mqtt_port = 1883

blue = (0, 0, 255)
white = (255, 255, 255)

def on_message(client, userdata, message):
    try:
        data = int(message.payload.decode('ascii'))
        print(f"Otrzymano: {data}")

        value = int(64 * data / 100)
        pixels = [blue if i < value else white for i in range(64)]
        sense.set_pixels(pixels)
    except ValueError:
        print("Odebrano niepoprawne dane!")

client = mqtt.Client("sub1")
client.on_message = on_message

try:
    client.connect(mqtt_broker_address, mqtt_port)
    client.subscribe("humidity")
    client.loop_start()

    print("Subskrybuję temat 'humidity'...")
    
    while True:
        pass  

except Exception as e:
    print(f"Błąd: {e}")

finally:
    print("Zamykanie klienta MQTT...")
    client.loop_stop()
    client.disconnect()
