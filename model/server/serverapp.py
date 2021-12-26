from model.server.calculation_server import CalculationServer


if __name__ == '__main__':
    server_app = CalculationServer()
    server_app.listenClients()

