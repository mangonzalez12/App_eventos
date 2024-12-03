import sqlite3
import csv

# Connect to SQLite (or create the database if it doesn't exist)
connection = sqlite3.connect("eventos.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the 'eventos' table if it doesn't exist
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

# Commit the creation of the table
connection.commit()

# Specify the CSV file to import
csv_file = "input_data.csv"  # Replace with the actual file path

# Open and read the CSV file
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)  # Use DictReader for column-based insertion
    for row in reader:
        # Insert each row into the database
        cursor.execute("""
        INSERT INTO eventos (Evento, Lugar, Fecha, Numero_participantes, Invitaciones_confirmadas, Expositores, Temas, Documentos, Materiales_de_apoyo, Otros_recursos)
        VALUES (:Evento, :Lugar, :Fecha, :Numero_participantes, :Invitaciones_confirmadas, :Expositores, :Temas, :Documentos, :Materiales_de_apoyo, :Otros_recursos)
        """, row)

# Commit the changes
connection.commit()

# Close the connection
connection.close()

print("Data imported into eventos.db successfully!")
