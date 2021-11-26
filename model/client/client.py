import socket
from socket import socket
from model.core.command_request import ComandRequest
from model.core.operators import Operators


class Client:
    SERVERIP = "localhost"  # 127.0.0.1
    PORT = 9043

    def __init__(self):
        self._clientSocket = socket()  # Socket.AF_INET, Socket.SOCK_STREAM
        self._clientSocket.connect((Client.SERVERIP, Client.PORT))
        self._operators = {"+": Operators.ADD, "-": Operators.SUB, "#": Operators.EXIT}

    def communicate(self):
        while True:
            try:
                op = input("Enter operator:")
                operands = eval(input("Enter numbers:"))
                cr = ComandRequest(op, operands)
                self._clientSocket.send(cr.encode())
                if cr == "exit":
                    break
                msg = self._clientSocket.recv(1024)
                print(msg.decode())
            except socket.error as err:
                pass

    def close_client(self):
        self._clientSocket.close()
