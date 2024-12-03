import sqlite3

# Connect to SQLite (or create the database)
connection = sqlite3.connect("eventos.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS eventos (
    Evento TEXT,
    Lugar TEXT,
    Fecha TEXT,
    Numero_participantes INTEGER,
    Invitaciones_confirmadas INTEGER,
    Expositores TEXT,
    Temas TEXT,
    Documentos TEXT,
    Materiales_de_apoyo TEXT,
    Otros_recursos TEXT
)
""")

# Insert data into the table
data = [
    ("Evento1", "Lugar1", "2024-12-01", 100, 80, "Expositor1|Expositor2", "Temas1|Temas2", "Documento1.pdf", "Material1|Material2", "Recurso1"),
    ("Evento2", "Lugar2", "2024-12-05", 50, 40, "Expositor3", "Temas3", "Documento2.pdf", "Material3", "Recurso2")
]

cursor.executemany("""
INSERT INTO eventos (Evento, Lugar, Fecha, Numero_participantes, Invitaciones_confirmadas, Expositores, Temas, Documentos, Materiales_de_apoyo, Otros_recursos)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", data)

# Commit changes and close the connection
connection.commit()
connection.close()

print("SQLite database created and data inserted!")

