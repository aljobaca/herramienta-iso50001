from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__, static_folder="../static", template_folder="../templates")

app.secret_key = "clave_secreta_para_validaciones"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Datos del formulario enviados desde el cliente
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Validaciones
        if password != confirm_password:
            return jsonify({"status": "error", "message": "Las contraseñas no coinciden."})
        if len(password) < 8:
            return jsonify({"status": "error", "message": "La contraseña debe tener al menos 8 caracteres."})

        # Llamar a un servicio en PHP (si es necesario)
        return jsonify({"status": "success", "message": "Usuario registrado correctamente."})

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
