import socket

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))

    def recive():
        while True:
           
                msg = client.recv(1024).decode()
                print(msg)
           
                break

    threading.Thread(target=recive, daemon=True).start()

    while True:
        msg = input()
        client.send(msg.encode())
      
            
    
        client.close()
if __name__ == '__main__':
    import threading
    client_program() 

