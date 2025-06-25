# 🌌 SpaceWallet

**Converta seu saldo em reais para dólares e compre imagens reais do espaço diretamente da NASA!**
Um projeto divertido, didático e totalmente funcional usando **Python + APIs + POO**.

---

## 📸 Visão geral

Este projeto simula uma **compra de imagens da NASA** utilizando seu saldo em **Reais (BRL)**, convertido automaticamente para **Dólares (USD)** com base na cotação atual do mercado.
Se você tiver saldo suficiente em dólar, poderá "comprar" a imagem do dia e baixar ela direto para o seu computador.

---

## ✨ Funcionalidades

✅ Consulta a cotação do dólar em tempo real
✅ Converte seu saldo de R\$ para U\$
✅ Acessa a imagem do dia da NASA (via API oficial)
✅ Valida se há saldo suficiente para a compra
✅ Faz o "download" da imagem em alta resolução
✅ Registra o histórico de compras em `.json`

---

## 💼 Tecnologias utilizadas

* [x] Python 3.10+
* [x] Requests (requisições HTTP)
* [x] API AwesomeAPI (cotação do dólar)
* [x] API NASA - Astronomy Picture of the Day (APOD)
* [x] Programação Orientada a Objetos (POO)
* [x] JSON para salvar histórico

---

## 🧪 Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/HericRibeiro/SpaceWallet.git
cd SpaceWallet
```

2. Instale as dependências:

```bash
pip install requests
```

3. Execute o projeto:

```bash
python main.py
```

---

## 🗄️ Exemplo de execução

```
Digite quanto deseja investir: 500
O valor do dólar está: U$ 5.42
Seu saldo é de: U$: 92.25
❌ Compra não autorizada, invista mais!

OU

Digite quanto deseja investir: 1500
O valor do dólar está: U$ 5.42
Seu saldo é de: U$: 276.64
✅ Compra efetuada com sucesso!
📸 Título: Cosmic Fireworks in NGC 6946
📛 Descrição: Follow-up explicando a imagem...
```

A imagem será salva como `imagem_comprada.jpg` e o histórico em `historico_compras.json`.

---

## 📁 Estrutura de arquivos

```
SpaceWallet/
│
├── main.py                     # Script principal
├── conversao.py                # Conversão de moeda
├── nasa.py                     # Requisição da imagem
├── venda.py                    # Lógica de compra
├── utils.py                    # Download da imagem e histórico
├── historico_compras.json      # Histórico das compras
└── README.md                   # Este arquivo
```

---

## 🔮 Possíveis melhorias

* ✅ Interface gráfica com Streamlit ou Flask
* ✅ Múltiplas opções de imagens para comprar
* ✅ Integração com carteira virtual persistente
* ✅ Integração com banco de dados

---

## 👨‍💻 Autor

**Heric Ribeiro**
Desenvolvedor apaixonado por automações, APIs e experiências interativas com Python.
[🔗 LinkedIn](https://www.linkedin.com/in/heric-willian-5b78722a3/)
[GitHub](https://github.com/HericRibeiro)

---

## 🚀 Agradecimentos

* [AwesomeAPI](https://docs.awesomeapi.com.br/) pela API de cotações
* [NASA APOD API](https://api.nasa.gov/) por tornar o universo mais acessível 🌌

---

> *"O código te leva até a tela. A criatividade, até as estrelas."* 🚀
