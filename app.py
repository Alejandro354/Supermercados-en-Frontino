from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"


def get_db():
    conn = sqlite3.connect("supermercados.db")
    conn.row_factory = sqlite3.Row
    return conn


# ----------------------
# PÁGINA PRINCIPAL
# ----------------------
@app.route("/")
def index():
    query = request.args.get("q", "")
    conn = get_db()
    supermercados = conn.execute(
        "SELECT * FROM supermercados WHERE nombre LIKE ? OR direccion LIKE ?",
        (f"%{query}%", f"%{query}%")
    ).fetchall()

    return render_template(
        "index.html",
        supermercados=supermercados,
        query=query,
        admin=session.get("admin")
    )


# ----------------------
# LOGIN
# ----------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                            (username, password)).fetchone()

        if user:
            session["admin"] = username
            return redirect("/admin")
        else:
            error = "Usuario o contraseña incorrectos"

    return render_template("login.html", error=error)


# ----------------------
# PANEL ADMIN
# ----------------------
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("admin"):
        return redirect("/login")

    conn = get_db()

    # Procesar nuevo supermercado
    if request.method == "POST":
        nombre = request.form["nombre"]
        direccion = request.form["direccion"]
        horario = request.form.get("horario")
        telefono = request.form.get("telefono")
        imagen = request.form.get("imagen")

        conn.execute("""
            INSERT INTO supermercados (nombre, direccion, horario, telefono, imagen)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, direccion, horario, telefono, imagen))
        conn.commit()

        return redirect("/admin")

    supermercados = conn.execute("SELECT * FROM supermercados").fetchall()

    return render_template("admin.html", supermercados=supermercados, admin=session.get("admin"))


# ----------------------
# LOGOUT
# ----------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
