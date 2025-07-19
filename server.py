import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("nombre de la computadora (servidor): " + hostname)
print("dirección ip" + ip)



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen()
client, address = server_socket.accept() 
print("Se conectó un cliente desde: " + str(address))
print("Servidor escuchando en el puerto 12345...")

clients = {} 

while True:



    try:
        client.send("ingrese nom usuario".encode())
        username = client.recv(1024).decode().strip()


        clients[username] = client


        client.send("escribe (/oln  o /<usuario> ): ".encode())
        option = client.recv(1024).decode().strip()

        if option == "/oln":
            client.send("mensaje a todos ".encode())
            msg = client.recv(1024).decode()

        
            for user, sock in clients.items():
                        sock.send(f"[{username}] dice: {msg}\n".encode())
                    
        elif option.startswith("/"):
            dest = option[1:]
            client.send("mnsj privado ".encode())
            msg = client.recv(1024).decode()

            if dest in clients:
                    clients[dest].send(f"[mnsj de: {username}] {msg}\n".encode())
          
            else:
                client.send("no se encontro usuario\n".encode())
        else:
            client.send("no existe esta opcion\n".encode())

   

    finally:

        if username in clients:
            del clients[username]
        client.close()