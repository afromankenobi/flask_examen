from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])

        precio = 9000
        total_sin_descuento = tarros * precio

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_final = total_sin_descuento * (1 - descuento)

        return render_template(
            "ejercicio1.html",
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            total_final=total_final
        )

    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("ejercicio2.html", mensaje=mensaje)

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
