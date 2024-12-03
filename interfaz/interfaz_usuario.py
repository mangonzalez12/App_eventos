import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to save data to SQLite database
def save_data():
    evento = evento_entry.get()
    lugar = lugar_entry.get()
    fecha = fecha_entry.get()
    num_part = numero_participantes_entry.get()
    inv_conf = invitaciones_confirmadas_entry.get()

    # Simple validation
    if not evento or not lugar or not fecha:
        messagebox.showerror("Error", "Please fill in all required fields!")
        return

    # Insert data into the database
    try:
        connection = sqlite3.connect("eventos.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO eventos (Evento, Lugar, Fecha, Numero_participantes, Invitaciones_confirmadas)
        VALUES (?, ?, ?, ?, ?)""", (evento, lugar, fecha, num_part, inv_conf))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Data saved successfully!")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to clear input fields
def clear_fields():
    evento_entry.delete(0, tk.END)
    lugar_entry.delete(0, tk.END)
    fecha_entry.delete(0, tk.END)
    numero_participantes_entry.delete(0, tk.END)
    invitaciones_confirmadas_entry.delete(0, tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("Eventos Manager")

# Input fields
tk.Label(root, text="Evento:").grid(row=0, column=0, padx=10, pady=5)
evento_entry = tk.Entry(root)
evento_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Lugar:").grid(row=1, column=0, padx=10, pady=5)
lugar_entry = tk.Entry(root)
lugar_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
fecha_entry = tk.Entry(root)
fecha_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Numero participantes:").grid(row=3, column=0, padx=10, pady=5)
numero_participantes_entry = tk.Entry(root)
numero_participantes_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Invitaciones confirmadas:").grid(row=4, column=0, padx=10, pady=5)
invitaciones_confirmadas_entry = tk.Entry(root)
invitaciones_confirmadas_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Save", command=save_data).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Clear", command=clear_fields).grid(row=5, column=1, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
