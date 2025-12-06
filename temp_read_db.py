import sqlite3
import os
#Creado para sacar la data de Sqlite
db_path = 'facturas.db'
if not os.path.exists(db_path):
    print("La base de datos no existe.")
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_archivo, numero_paginas, cufe, peso_archivo FROM facturas")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No hay datos en la tabla de facturas.")
    else:
        print("| Nombre del archivo | Numero de paginas | CUFE | Peso del archivo (MB) |")
        print("|---|---|---|---|")
        for row in rows:
            print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]:.4f} |")
