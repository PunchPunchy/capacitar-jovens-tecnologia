from flask import Flask, render_template, request
from datetime import datetime
import csv
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def quiz():
    resultado = None
    feedback_enviado = False

    if request.method == "POST":
        nome = request.form["nome"]
        resposta1 = request.form["resposta1"]
        resposta2 = request.form["resposta2"]
        resposta3 = request.form["resposta3"]

        pontuacao = 0

        if resposta1 == "A":
            pontuacao += 1

        if resposta2 == "B":
            pontuacao += 1

        if resposta3 == "B":
            pontuacao += 1

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        resultado = {
            "nome": nome,
            "pontuacao": pontuacao,
            "data": data
        }

    return render_template(
        "index.html",
        resultado=resultado,
        feedback_enviado=feedback_enviado
    )


@app.route("/feedback", methods=["POST"])
def feedback():
    nome = request.form["nome"]
    pontuacao = request.form["pontuacao"]
    data = request.form["data"]

    avaliacao = request.form["avaliacao"]
    aprendizado = request.form["aprendizado"]
    comentario = request.form["comentario"]

    arquivo = "feedbacks.csv"

    arquivo_existe = os.path.exists(arquivo)

    with open(arquivo, "a", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f)

        if not arquivo_existe:
            escritor.writerow([
                "Nome",
                "Pontuação",
                "Data e Hora",
                "Avaliação",
                "Aprendizado",
                "Comentário"
            ])

        escritor.writerow([
            nome,
            pontuacao,
            data,
            avaliacao,
            aprendizado,
            comentario
        ])

    resultado = {
        "nome": nome,
        "pontuacao": pontuacao,
        "data": data
    }

    return render_template(
        "index.html",
        resultado=resultado,
        feedback_enviado=True
    )


if __name__ == "__main__":
    app.run(debug=True)