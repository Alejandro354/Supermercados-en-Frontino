import sqlite3

# Conexión
connection = sqlite3.connect('supermercados.db')
cursor = connection.cursor()

# -------------------------------
# TABLA DE SUPERMERCADOS
# -------------------------------

cursor.execute("DROP TABLE IF EXISTS supermercados")

cursor.execute("""
CREATE TABLE supermercados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    horario TEXT,
    telefono TEXT,
    imagen TEXT
)
""")

supermercados = [
    ("Supermercado Merkapues",
     "Frontino, Antioquia",
     "Abierto ⋅ Cierra a las 8:30 p.m.",
     "48595568",
     "merkapues.jpg"),

    ("Supermercado D1 De Todos, frontino",
     "Frontino, Antioquia",
     "Abierto ⋅ Cierra a las 8:30 p.m.",
     "",
     "D1frontino.jpg"),

    ("Merkemos parque Frontino",
     "Cra. 30 #29a56, Frontino, Antioquia",
     "Abierto ⋅ Cierra a las 8 p.m.",
     "3215474616",
     "merkemos_frontino.jpg"),

    ("Merkemos Manguruma Frontino",
     "Cra. 36 #21-42, Frontino, Antioquia",
     "Abre pronto · 9 a.m.",
     "01-800-0956886",
     "merkemos_maguruma.webp"),

    ("Minisuper la 18",
     "Cl. 18 #34-43, Frontino, Antioquia",
     "Abierto ⋅ Cierra a las 9 p.m.",
     "",
     "la_18.webp"),

    ("Tienda La Florida",
     "Cra. 36 # 15 - 159, Frontino, Antioquia",
     "Abierto ⋅ Cierra a las 9 p.m.",
     "",
     "florida.jpg"),

    ("Mercolanta Frontino",
     "Cra. 32 # 29-03, Frontino, Antioquia",
     "Abierto ⋅ Cierra a las 6 p.m.",
     "(604) 8595235",
     "mercolanta.webp"),

    ("SUPERMERCADO ECONOMIA",
     "Cra. 32 #2939, Frontino, Antioquia",
     "",
     "",
     "economia.jpg"),

    ("Tiendas D1 - Frontino Manguruma",
     "Cra. 36 #22-2 a 22-124, Frontino, Antioquia",
     "",
     "",
     "D1_manguruma.webp"),

    ("Depósito El Trapiche",
     "Cl. 35 #30-49 a 30-1, Frontino, Antioquia",
     "Abierto ⋅ Cierra a las 6 p.m.",
     "48595246",
     "trapiche.jpg")
]

cursor.executemany("""
INSERT INTO supermercados (nombre, direccion, horario, telefono, imagen)
VALUES (?, ?, ?, ?, ?)
""", supermercados)

# -------------------------------
# TABLA DE USUARIOS ADMIN
# -------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# Usuario administrador solicitado
cursor.execute("""
INSERT OR IGNORE INTO users (username, password)
VALUES ('luis', 'sena1')
""")

# Guardar cambios
connection.commit()
connection.close()

print("Base de datos creada correctamente con usuario admin.")
