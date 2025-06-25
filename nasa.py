import requests

class NasaImage:
    def __init__(self):
        self.api_key = "DEMO_KEY"
        self.preco = 200

    def get_dados(self):
        url = f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}"
        response = requests.get(url).json()
        return response

