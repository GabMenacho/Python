from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST", "DELETE"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            
            if (request.form["operacao"] == "soma"):
                operacao = "soma"
                resultado = int(num1) + int(num2)

            elif (request.form["operacao"] == "sub"):
                operacao = "subtração"
                resultado = int(num1) - int(num2)

            elif (request.form["operacao"] == "mult"):
                operacao = "multiplicação"
                resultado = int(num1) * int(num2)

            elif (request.form["operacao"] == "div"):
                operacao = "divisão"
                resultado = int(num1) / int(num2)

            return ("O resultado da " + (operacao) + " é igual a: " + str(resultado))

        else:
            return "Campo vazio. Informe um valor numérico!"


@app.errorhandler(404)
def not_found(error):
    return render_template("erro.html")


app.run(port=8080, debug=True)