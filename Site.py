from flask import Flask, render_template, request, url_for, redirect

app = Flask(
    __name__, template_folder="C:\Projetos\Roadmap Python\Live Flask\Templates")


@app.route('/', methods=["GET","POST"])
def Pagprincial():
    if request.method == "POST":
        user= request.form.get("nome")
        email=request.form.get("email")
        senha=request.form.get("senha")
        return redirect(url_for("usuarios",user=user,email=email))
    return render_template("Pagprincipal.html")

@app.route("/usuarios/<user>")
def usuarios(user):
    user=user 
    email= request.args.get('email',None)
    return render_template("usuarios.html", user=user,email=email)


@app.route('/contatos')
def contatos():
    return render_template('contatos.html', empresa="roadmappython")


@app.route("/admin")
def admin():
    return redirect(url_for('contatos'))



@app.route("/<string:palavra>")
def erro(palavra):
    return "Erro 404 pagina {} não encontrada".format(palavra)


if __name__ == '__main__':
    app.run(debug=True)
