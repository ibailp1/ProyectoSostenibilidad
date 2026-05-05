from flask import Flask, render_template, request, jsonify
from datetime import datetime, date
import sqlite3, os

app = Flask(__name__)
DB = "reciclapp.db"

CATEGORIAS = {
    "Ratón": {"icono": "🖱️", "grupo": "Periféricos"},
    "Teclado": {"icono": "⌨️", "grupo": "Periféricos"},
    "Cable USB": {"icono": "🔌", "grupo": "Cables"},
    "Cable HDMI": {"icono": "🔌", "grupo": "Cables"},
    "Cable de red": {"icono": "🌐", "grupo": "Cables"},
    "Cargador": {"icono": "⚡", "grupo": "Cables"},
    "Móvil": {"icono": "📱", "grupo": "Móviles"},
    "Tablet": {"icono": "📟", "grupo": "Móviles"},
    "Portátil": {"icono": "💻", "grupo": "Ordenadores"},
    "Ordenador de sobremesa": {"icono": "🖥️", "grupo": "Ordenadores"},
    "Monitor": {"icono": "🖥️", "grupo": "Ordenadores"},
    "Impresora": {"icono": "🖨️", "grupo": "Impresoras"},
    "Batería": {"icono": "🔋", "grupo": "Baterías"},
    "Pila": {"icono": "🔋", "grupo": "Baterías"},
    "Auriculares": {"icono": "🎧", "grupo": "Audio"},
    "Altavoz": {"icono": "🔊", "grupo": "Audio"},
    "Disco duro": {"icono": "💾", "grupo": "Almacenamiento"},
    "Pendrive": {"icono": "💾", "grupo": "Almacenamiento"},
    "Router": {"icono": "📡", "grupo": "Red"},
    "Otro": {"icono": "♻️", "grupo": "Otros"},
}

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                elemento TEXT NOT NULL,
                cantidad INTEGER NOT NULL DEFAULT 1,
                fecha DATE NOT NULL,
                hora TIME NOT NULL,
                creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

@app.route("/")
def formulario():
    return render_template("formulario.html", categorias=CATEGORIAS)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/registrar", methods=["POST"])
def registrar():
    data = request.get_json()
    elementos = data.get("elementos", [])
    if not elementos:
        return jsonify({"error": "Sin elementos"}), 400
    hoy = date.today().isoformat()
    ahora = datetime.now().strftime("%H:%M:%S")
    with get_db() as conn:
        for elem in elementos:
            conn.execute(
                "INSERT INTO registros (elemento, cantidad, fecha, hora) VALUES (?, ?, ?, ?)",
                (elem["nombre"], elem["cantidad"], hoy, ahora)
            )
        conn.commit()
    return jsonify({"ok": True, "registrados": len(elementos)})

@app.route("/api/stats")
def stats():
    with get_db() as conn:
        total = conn.execute("SELECT SUM(cantidad) as t FROM registros").fetchone()["t"] or 0
        por_elemento = conn.execute("""
            SELECT elemento, SUM(cantidad) as total
            FROM registros GROUP BY elemento ORDER BY total DESC
        """).fetchall()
        hoy = date.today().isoformat()
        hoy_total = conn.execute(
            "SELECT SUM(cantidad) as t FROM registros WHERE fecha=?", (hoy,)
        ).fetchone()["t"] or 0
        hoy_elementos = conn.execute("""
            SELECT elemento, SUM(cantidad) as total
            FROM registros WHERE fecha=? GROUP BY elemento ORDER BY total DESC
        """, (hoy,)).fetchall()
        por_dia = conn.execute("""
            SELECT fecha, SUM(cantidad) as total
            FROM registros GROUP BY fecha ORDER BY fecha DESC LIMIT 30
        """).fetchall()
        ultimos = conn.execute("""
            SELECT elemento, cantidad, fecha, hora
            FROM registros ORDER BY creado_en DESC LIMIT 20
        """).fetchall()

    return jsonify({
        "total_global": total,
        "total_hoy": hoy_total,
        "por_elemento": [dict(r) for r in por_elemento],
        "hoy_elementos": [dict(r) for r in hoy_elementos],
        "por_dia": [dict(r) for r in por_dia],
        "ultimos": [dict(r) for r in ultimos],
        "categorias": CATEGORIAS,
    })

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
