import socket
import requests

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("servidor" + hostname)
print("la direccion ip es: " + ip)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, 12345))
server_socket.listen(1)  

while True:
    client_socket, address = server_socket.accept()
    print("se conecta cliente:" + str(address))
   
    client_socket.send("ingrese nombre".encode())

    nom = client_socket.recv(1024).decode().strip()
    print("Usuario recibido: " + nom)

    while True:
 
        client_socket.send("Escribe  (no o chau): ".encode())

        c= client_socket.recv(1024).decode().strip()

        if c == "no":
            try:
                recuest = requests.get("https://rickandmortyapi.com/api/character/160")
                data = recuest.json()

                ag = [a["displayName"] for a in data["data"]]
                mnsj = f"buenas {nom}, esto es un personaje d rick y morty:\n" + "\n".join(ag)
            except Exception as e:
                mnsj = "Error."

            client_socket.send(mnsj.encode())

        elif c == "chau":
            adios  = f"chau, {nom}."
            client_socket.send(adios.encode())
            print(f"el cliente {nom} se cnecto.")
            break
        else:
            client_socket.send("Comando no esta mal. no o chau\n".encode())

    client_socket.close()
