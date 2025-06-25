import requests

class Conversao:
    def __init__(self, saldo):
        self.saldo = saldo
        self.dolar = 0.0

    def cotacao(self):
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url).json()
        self.dolar = float(response["USDBRL"]["high"])

    def saldo_convertido(self):
        self.cotacao()
        return self.saldo / self.dolar
