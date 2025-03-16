from sense_emu import SenseHat
import socket
sense = SenseHat()
# Konfiguracja gniazda TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.146', 4050)
sock.bind(server_address)
sock.listen(1)  # Nasłuchuj tylko jednego klienta
# Kolory
green = (0, 255, 0)
white = (255, 255, 255)
print("Serwer TCP oczekuje na połączenie...")
connection, client_address = sock.accept()
print(f"Połączono z: {client_address}")
try:
   buffer = ''
   while True:
       data = connection.recv(64)  # Odbierz dane
       if not data:
           break
       # Parsuj dane (format: "wartość\n")
       buffer += data.decode('ascii')
       if '\n' in buffer:
           line, buffer = buffer.split('\n', 1)
           value = int(line.strip())
           print(f"Odebrano: {value}%")
           # Aktualizuj diody LED
           pixels = [green if i < (64 * value / 100) else white for i in range(64)]
           sense.set_pixels(pixels)
finally:
   connection.close()
   sock.close()