from nasa import NasaImage
from conversao import Conversao
from utils import salvar_imagem, salvar_historico

def venda_da_imagem(saldo_usuario):
    nasa = NasaImage()
    user = Conversao(saldo_usuario)
    saldo_dolar = user.saldo_convertido()
    
    if saldo_dolar >= nasa.preco:
        dados = nasa.get_dados()
        salvar_imagem(dados["url"])
        salvar_historico(dados["title"], dados["url"], nasa.preco)
        print(f"\n✅ Compra feita! Acesse sua imagem: {dados['url']}")
        print(f"🖼️ Título: {dados['title']}")
        print(f"📚 Descrição: {dados['explanation'][:200]}...")
    else:
        print("❌ Saldo insuficiente.")
