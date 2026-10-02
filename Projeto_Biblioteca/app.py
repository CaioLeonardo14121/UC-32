from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

BANCO = "biblioteca.db"


def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/")
def index():
    conexao = conectar()

    autores = conexao.execute(
        "SELECT COUNT(*) AS total FROM autores"
    ).fetchone()["total"]

    livros = conexao.execute(
        "SELECT COUNT(*) AS total FROM livros"
    ).fetchone()["total"]

    leitores = conexao.execute(
        "SELECT COUNT(*) AS total FROM leitores"
    ).fetchone()["total"]

    conexao.close()

    return render_template(
        "index.html",
        autores=autores,
        livros=livros,
        leitores=leitores
    )


# AUTORES
@app.route("/autores")
def autores():
    conexao = conectar()
    dados = conexao.execute(
        "SELECT * FROM autores ORDER BY nome"
    ).fetchall()
    conexao.close()

    return render_template("autores.html", autores=dados)


@app.route("/autores/cadastrar", methods=["POST"])
def cadastrar_autor():
    nome = request.form["nome"]

    conexao = conectar()
    conexao.execute(
        "INSERT INTO autores (nome) VALUES (?)",
        (nome,)
    )
    conexao.commit()
    conexao.close()

    return redirect("/autores")


@app.route("/autores/excluir/<int:id>")
def excluir_autor(id):
    conexao = conectar()
    conexao.execute(
        "DELETE FROM autores WHERE id_autor = ?",
        (id,)
    )
    conexao.commit()
    conexao.close()

    return redirect("/autores")


# LIVROS
@app.route("/livros")
def livros():
    conexao = conectar()

    dados = conexao.execute("""
        SELECT livros.id_livro,
               livros.titulo,
               livros.ano,
               autores.nome AS autor
        FROM livros
        LEFT JOIN autores
        ON livros.id_autor = autores.id_autor
        ORDER BY livros.titulo
    """).fetchall()

    autores = conexao.execute(
        "SELECT * FROM autores ORDER BY nome"
    ).fetchall()

    conexao.close()

    return render_template(
        "livros.html",
        livros=dados,
        autores=autores
    )


@app.route("/livros/cadastrar", methods=["POST"])
def cadastrar_livro():
    titulo = request.form["titulo"]
    ano = request.form["ano"]
    id_autor = request.form["id_autor"]

    conexao = conectar()
    conexao.execute("""
        INSERT INTO livros (titulo, ano, id_autor)
        VALUES (?, ?, ?)
    """, (titulo, ano, id_autor))

    conexao.commit()
    conexao.close()

    return redirect("/livros")


@app.route("/livros/excluir/<int:id>")
def excluir_livro(id):
    conexao = conectar()
    conexao.execute(
        "DELETE FROM livros WHERE id_livro = ?",
        (id,)
    )
    conexao.commit()
    conexao.close()

    return redirect("/livros")


# LEITORES
@app.route("/leitores")
def leitores():
    conexao = conectar()

    dados = conexao.execute("""
        SELECT * FROM leitores
        ORDER BY nome
    """).fetchall()

    conexao.close()

    return render_template(
        "leitores.html",
        leitores=dados
    )


@app.route("/leitores/cadastrar", methods=["POST"])
def cadastrar_leitor():
    nome = request.form["nome"]
    email = request.form["email"]

    conexao = conectar()
    conexao.execute("""
        INSERT INTO leitores (nome, email)
        VALUES (?, ?)
    """, (nome, email))

    conexao.commit()
    conexao.close()

    return redirect("/leitores")


@app.route("/leitores/excluir/<int:id>")
def excluir_leitor(id):
    conexao = conectar()
    conexao.execute(
        "DELETE FROM leitores WHERE id_leitor = ?",
        (id,)
    )
    conexao.commit()
    conexao.close()

    return redirect("/leitores")


if __name__ == "__main__":
    app.run(debug=True)