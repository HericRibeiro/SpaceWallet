import requests, json

def salvar_imagem(url, nome_arquivo="imagem_comprada.jpg"):
    img = requests.get(url).content
    with open(nome_arquivo, "wb") as f:
        f.write(img)

def salvar_historico(titulo, url, preco):
    compra = {"titulo": titulo, "url": url, "preco": preco}
    with open("historico_compras.json", "a", encoding="utf-8") as f:
        json.dump(compra, f, ensure_ascii=False)
        f.write(",\n")
