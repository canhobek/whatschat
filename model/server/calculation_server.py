from socket import socket as Socket


class CalculationServer:
    PORT = 9043

    def __init__(self):
        self._severSocket = Socket()  # Socket.AF_INET, Socket.SOCK_STREAM
        self._severSocket.bind(("", CalculationServer.PORT))
        self._severSocket.listen(10)


    def listenClients(self):
        while True:
            clientSocket, _ = self._severSocket.accept()  # tuple unpack
            self.handle_client(clientSocket)



    def handle_client(self, clientSocket):
        while True:
            msg = clientSocket.recv(1024).decode()
            if msg == "exit":
                break
            clientSocket.send(("Server" + msg).encode())

        print("Connection ends")
        self._severSocket.close()
        clientSocket.close()