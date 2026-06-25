# 📦 Sistema de Controle de Estoque e Vendas

Um sistema desktop para gerenciamento de inventário de produtos e registro de vendas em tempo real. Desenvolvido em Python com a biblioteca gráfica **Tkinter**, aplicando conceitos consolidados de **Programação Orientada a Objetos (POO)**.

---

## 🚀 Funcionalidades

* **Cadastro de Produtos:** Registro de itens informando nome, preço e quantidade inicial em estoque.
* **Validação de Tipos de Dados:** Sistema protegido contra campos vazios e erros de conversão de dados (ex: digitar letras no preço ou quantidade).
* **Interface Interativa (`Listbox`):** Exibição dos produtos em uma lista clicável, permitindo selecionar o item diretamente na tela para realizar operações.
* **Gerenciamento de Vendas:** Diminui automaticamente a quantidade do produto selecionado ao registrar uma venda e valida se há estoque suficiente antes de concluir a operação.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica:** Tkinter (Nativo do Python)
* **Paradigma:** Programação Orientada a Objetos (POO)

---

## 📁 Estrutura do Projeto

* `classes.py`: Contém a modelagem das entidades do sistema:
  * `Produto`: Classe que representa o item, seus atributos e regras de negócio.
  * `Estoque`: Classe responsável por gerenciar a coleção de produtos (adicionar, listar).
  * `Venda`: Classe preparada para futuras expansões e históricos de vendas.
* `app.py`: Arquivo principal que renderiza a interface gráfica, captura os eventos do usuário e faz a ponte com a lógica do estoque.

---

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Baixe ou clone os arquivos `app.py` e `classes.py` na mesma pasta.
3. Se estiver utilizando Linux (como Kubuntu) e o Tkinter não estiver instalado por padrão, execute no terminal:
   ```bash
   sudo apt install python3-tk
