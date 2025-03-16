from sense_emu import SenseHat
from time import sleep
import socket
sense = SenseHat()
# Konfiguracja gniazda TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote_address = ('192.168.0.146', 4050)
sock.connect(remote_address)  # Nawiąż połączenie
try:
   while True:
       humidity = round(sense.humidity)
       # Wyślij dane w formacie "wartość\n"
       message = f"{humidity}\n"
       sock.sendall(message.encode('ascii'))
       sleep(0.1)
except KeyboardInterrupt:
   print("Zamykanie połączenia...")
   sock.close()