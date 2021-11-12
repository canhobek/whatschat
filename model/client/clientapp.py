from model.client.client import Client

if __name__ == '__main__':
    cApp = Client()
    cApp.communicate()

    cApp.close_client()