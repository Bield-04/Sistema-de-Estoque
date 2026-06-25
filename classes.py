class Produto :
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}"
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome_produto):
        self.produtos = [produto for produto in self.produtos if produto.nome != nome_produto]

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)
class Venda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def realizar_venda(self):
        if self.produto.quantidade >= self.quantidade:
            self.produto.atualizar_quantidade(self.produto.quantidade - self.quantidade)
            print(f"Venda realizada: {self.quantidade} unidades de {self.produto.nome}")
        else:
            print(f"Quantidade insuficiente em estoque para {self.produto.nome}")
