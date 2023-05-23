import socket
import json

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asigna una dirección y puerto al socket
server_address = ('25.35.176.44', 1234)  # Dirección IP y puerto del servidor
sock.bind(server_address)

# Escucha conexiones entrantes
sock.listen(1)

print('Esperando conexiones entrantes...')

while True:
    # Espera una conexión
    client_socket, client_address = sock.accept()
    print('Conexión establecida desde:', client_address)

    # Recibe los datos del cliente
    data = client_socket.recv(1024)
    print('Datos recibidos:', data.decode())
    _data = json.loads(data.decode())
    print(_data)
    

    # Envía una respuesta al cliente
    response = 'Hola, cliente!'
    client_socket.sendall(response.encode())
    # Cierra la conexión con el cliente
    client_socket.close()

