from classes import Produto, Estoque, Venda
from tkinter import Tk, Label, Entry, Button, Listbox, END

janela = Tk()
janela.title("Sistema de Estoque e Vendas")
janela.geometry("800x650")

# Lista global (ou você pode usar uma lista dentro da sua classe Estoque se preferir)
historico_vendas = []

# --- FUNÇÕES PARA INTERAGIR COM O ESTOQUE ---

def cadastrar_produto():
    nome = entry_nome.get()
    preco_texto = entry_preco.get()
    qtd_texto = entry_quantidade.get()
    
    if nome and preco_texto and qtd_texto:
        try:
            preco = float(preco_texto)
            quantidade = int(qtd_texto)
            
            produto = Produto(nome, preco, quantidade)
            estoque.adicionar_produto(produto)
            
            atualizar_lista_produtos()
            entry_nome.delete(0, END)
            entry_preco.delete(0, END)
            entry_quantidade.delete(0, END)
            label_venda_status.config(text="Produto cadastrado com sucesso!", fg="green")
        except ValueError:
            label_venda_status.config(text="Preço ou Quantidade inválidos no cadastro.", fg="red")
    else:
        label_venda_status.config(text="Por favor, preencha todos os campos do cadastro.", fg="red")

def atualizar_lista_produtos():
    listbox_produtos.delete(0, END)
    for produto in estoque.produtos:
        listbox_produtos.insert(END, f"{produto.nome} - Preço: R${produto.preco:.2f} - Qtd: {produto.quantidade}")

def atualizar_lista_vendas():
    listbox_vendas.delete(0, END)
    for venda in historico_vendas:
        # Ajuste os atributos (.produto.nome, .quantidade) de acordo com a sua classe Venda
        total = venda.produto.preco * venda.quantidade
        listbox_vendas.insert(END, f"{venda.quantidade}x {venda.produto.nome} - Total: R${total:.2f}")

# FUNÇÃO: REALIZAR A VENDA
def realizar_venda():
    try:
        # 1. Pega o índice do produto selecionado na Listbox de produtos
        selecao = listbox_produtos.curselection()
        
        if not selecao:
            label_venda_status.config(text="Selecione um produto na lista para vender!", fg="red")
            return
            
        indice = selecao[0]
        produto_selecionado = estoque.produtos[indice]
        
        # 2. Pega a quantidade que o usuário quer vender
        qtd_venda = int(entry_venda_qtd.get())
        
        if qtd_venda <= 0:
            label_venda_status.config(text="A quantidade deve ser maior que zero!", fg="red")
            return

        # 3. Verifica se tem estoque suficiente
        if qtd_venda <= produto_selecionado.quantidade:
            # Diminui do estoque
            produto_selecionado.quantidade -= qtd_venda
            
            # Cria o objeto Venda e adiciona no histórico
            nova_venda = Venda(produto_selecionado, qtd_venda)
            historico_vendas.append(nova_venda)
            
            # Atualiza a interface
            label_venda_status.config(text=f"Venda de {qtd_venda}x {produto_selecionado.nome} realizada!", fg="green")
            atualizar_lista_produtos()
            atualizar_lista_vendas()
            entry_venda_qtd.delete(0, END)
        else:
            label_venda_status.config(text=f"Estoque insuficiente! Apenas {produto_selecionado.quantidade} disponíveis.", fg="red")
            
    except ValueError:
        label_venda_status.config(text="Digite uma quantidade válida para a venda!", fg="red")


# --- CRIANDO O ESTOQUE ---
estoque = Estoque()

# --- ELEMENTOS DA INTERFACE (CADASTRO) ---
label_titulo = Label(janela, text="--- CADASTRO DE PRODUTOS ---", font=("Arial", 12, "bold"))
label_titulo.pack(pady=5)

label_nome = Label(janela, text="Nome do Produto:")
label_nome.pack()
entry_nome = Entry(janela)
entry_nome.pack()

label_preco = Label(janela, text="Preço do Produto:")
label_preco.pack()
entry_preco = Entry(janela)
entry_preco.pack()

label_quantidade = Label(janela, text="Quantidade Inicial:")
label_quantidade.pack()
entry_quantidade = Entry(janela)
entry_quantidade.pack()

button_cadastrar = Button(janela, text="Cadastrar Produto", bg="green", fg="white", command=cadastrar_produto)
button_cadastrar.pack(pady=10)


# --- ELEMENTOS DA INTERFACE (PRODUTOS EM ESTOQUE) ---
label_titulo_lista = Label(janela, text="--- PRODUTOS EM ESTOQUE ---", font=("Arial", 12, "bold"))
label_titulo_lista.pack(pady=5)

listbox_produtos = Listbox(janela, width=60, height=6)
listbox_produtos.pack(pady=5)

label_venda_qtd = Label(janela, text="Quantidade para Vender:")
label_venda_qtd.pack()
entry_venda_qtd = Entry(janela)
entry_venda_qtd.pack()

button_vender = Button(janela, text="💸 Registrar Venda do Item Selecionado", bg="blue", fg="white", command=realizar_venda)
button_vender.pack(pady=10)


# --- ELEMENTOS DA INTERFACE (HISTÓRICO DE VENDAS) ---
label_titulo_venda = Label(janela, text="--- HISTÓRICO DE VENDAS ---", font=("Arial", 12, "bold"))
label_titulo_venda.pack(pady=5)

listbox_vendas = Listbox(janela, width=60, height=6)
listbox_vendas.pack(pady=5)


# Label para status (mensagens de erro ou sucesso)
label_venda_status = Label(janela, text="", font=("Arial", 10, "bold"))
label_venda_status.pack(pady=5)

janela.mainloop()
