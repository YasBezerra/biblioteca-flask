# models.py

# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano, genero, quantidade, estrela=0, observacao=""):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.quantidade = quantidade
        self.estrela = estrela
        self.observacao = observacao

    def __str__(self):
        obs = f" | Obs: {self.observacao}" if self.observacao else ""
        return f"{self.titulo} | {self.autor} | {self.ano} | {self.genero} | Quantidade: {self.quantidade} | Estrelas: {self.estrela}{obs}"


# Lista em memória
biblioteca = []

# Função para cadastrar livro
def cadastrar_livro(titulo, autor, ano, genero, quantidade, estrela=0, observacao =""):
    livro = Livro(titulo, autor, ano, genero, quantidade, estrela, observacao)
    biblioteca.append(livro)

# Função para editar livro
def editar_livro(index, titulo, autor, ano, genero, quantidade, estrela=0, observacao=""):
    if 0 <= index < len(biblioteca):
        livro = biblioteca[index]
        livro.titulo = titulo
        livro.autor = autor
        livro.ano = ano
        livro.genero = genero
        livro.quantidade = quantidade
        livro.estrela = estrela
        livro.observacao = observacao

# Função para remover livro
def remover_livro(index):
    if 0 <= index < len(biblioteca):
        biblioteca.pop(index)

# Função para buscar livros por título (case-insensitive)
def buscar_livros(nome):
    nome = nome.lower()
    return [livro for livro in biblioteca if nome in livro.titulo.lower()]
