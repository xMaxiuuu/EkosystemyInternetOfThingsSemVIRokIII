from sense_emu import SenseHat
from time import sleep
import socket
sense = SenseHat()
print('Dziala')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
remote_address = ('100.101.5.175', 4050) #<--- Address
green = (0,255,0)
white = (255,255,255)

while True:
    humidity = round(sense.humidity)
    sock.sendto(bytes(str(humidity),'ascii'), remote_address)
    sleep(0.1)