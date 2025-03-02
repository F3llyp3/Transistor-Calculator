from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Coleta os dados e evita erro de conversão
        calculo = request.form["calculo"]
        
        def get_float(value):
            try:
                return float(value) if value else 0.0
            except ValueError:
                return 0.0  # Se não puder converter, assume 0.0
        
        vcc = get_float(request.form.get("vcc", "0"))
        rb = get_float(request.form.get("rb", "0"))
        rc = get_float(request.form.get("rc", "0"))
        beta = get_float(request.form.get("beta", "0"))

        # Inicializar resultados
        resultados = {}

        # Cálculo dependendo da escolha
        vbe = 0.7  # Tensão Base-Emissor (silício)
        if calculo == "ib" and rb > 0:
            ib = (vcc - vbe) / rb
            resultados["ib"] = ib
        elif calculo == "ic" and rb > 0 and beta > 0:
            ib = (vcc - vbe) / rb
            ic = beta * ib
            resultados["ic"] = ic
        elif calculo == "vce" and rb > 0 and beta > 0 and rc > 0:
            ib = (vcc - vbe) / rb
            ic = beta * ib
            vce = vcc - ic * rc
            resultados["vce"] = vce

        return render_template("index.html", resultados=resultados)

    # Se for GET, apenas exibir o formulário
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
