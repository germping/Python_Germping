import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_archivo TEXT NOT NULL,
                numero_paginas INTEGER NOT NULL,
                cufe TEXT NOT NULL,
                peso_archivo REAL NOT NULL
            )
        ''')

    def insert_factura(self, nombre_archivo, numero_paginas, cufe, peso_archivo):
        self.cursor.execute('''
            INSERT INTO facturas (nombre_archivo, numero_paginas, cufe, peso_archivo)
            VALUES (?, ?, ?, ?)
        ''', (nombre_archivo, numero_paginas, cufe, peso_archivo))
