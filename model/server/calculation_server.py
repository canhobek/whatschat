from socket import socket as Socket
from model.core.command_handler import CommandHandler

class CalculationServer:
    PORT = 9043

    def __init__(self):
        self._severSocket = Socket()  # Socket.AF_INET, Socket.SOCK_STREAM
        self._severSocket.bind(("", CalculationServer.PORT))
        self._severSocket.listen(10)
        self._is_alive = True
        self.__command_handler = CommandHandler()


    def listenClients(self):
        while self._is_alive:
            clientSocket, _ = self._severSocket.accept()  # tuple unpack
            self.handle_client(clientSocket)


    def handle_client(self, clientSocket):
        cmd = clientSocket.recv(1024).decode()


        result = self.__command_handler.execute_command(cmd)

        if result == None:
            self._is_alive = False

        clientSocket.send(str(result).encode())
        print("Calculation Completed ")
        clientSocket.close()