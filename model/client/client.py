import socket
from socket import socket

class Client:
    SERVERIP = "localhost" #127.0.0.1
    PORT = 9043
    def __init__(self):
        self._clientSocket = socket() #Socket.AF_INET, Socket.SOCK_STREAM
        self._clientSocket.connect((Client.SERVERIP, Client.PORT))



    def communicate(self):
        while True:
            try:
                send_msg = input("Enter a message")
                self._clientSocket.send(send_msg.encode())
                if send_msg == "exit":
                    break
                msg = self._clientSocket.recv(1024)
                print(msg.decode())
            except socket.error as err:
                pass


    def close_client(self):
        self._clientSocket.close()

