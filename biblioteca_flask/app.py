from flask import Flask, render_template, request, redirect, url_for
from models import Livro, biblioteca, cadastrar_livro

app = Flask(__name__)

# ===== Rota Menu Inicial =====
@app.route("/")
def home():
    return render_template("index.html")

# ===== Rota Cadastrar Livro =====
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor = request.form.get("autor", "").strip()
        ano = request.form.get("ano", "").strip()
        genero = request.form.get("genero", "").strip()
        quantidade_str = request.form.get("quantidade", "0").strip()
        observacao = request.form.get("observacao", "").strip()

        if not (titulo and autor and ano and genero and quantidade_str.isdigit()):
            return render_template("cadastrar.html", erro="Preencha todos os campos corretamente.")

        quantidade = int(quantidade_str)
        cadastrar_livro(titulo, autor, ano, genero, quantidade, observacao)
        return redirect(url_for("lista_livros"))

    return render_template("cadastrar.html")

# ===== Rota Editar Livro =====
@app.route("/editar/<int:index>", methods=["GET", "POST"])
def editar(index):
    if 0 <= index < len(biblioteca):
        livro = biblioteca[index]

        if request.method == "POST":
            livro.titulo = request.form.get("titulo", livro.titulo).strip()
            livro.autor = request.form.get("autor", livro.autor).strip()
            livro.ano = request.form.get("ano", livro.ano).strip()
            livro.genero = request.form.get("genero", livro.genero).strip()
            quantidade_str = request.form.get("quantidade", str(livro.quantidade)).strip()
            livro.observacao = request.form.get("observacao", livro.observacao).strip()

            if quantidade_str.isdigit():
                livro.quantidade = int(quantidade_str)

            return redirect(url_for("lista_livros"))

        return render_template("editar.html", livro=livro, index=index)
    return redirect(url_for("lista_livros"))

# ===== Rota Remover Livro =====
@app.route("/remover/<int:index>")
def remover(index):
    if 0 <= index < len(biblioteca):
        biblioteca.pop(index)
    return redirect(url_for("lista_livros"))

# ===== Rota Lista de Livros =====
@app.route("/livros")
def lista_livros():
    busca = request.args.get("busca", "").strip().lower()
    if busca:
        livros_filtrados = [livro for livro in biblioteca if busca in livro.titulo.lower()]
    else:
        livros_filtrados = biblioteca
    return render_template("lista_livros.html", livros=livros_filtrados, busca=busca)

if __name__ == "__main__":
    app.run(debug=True)
