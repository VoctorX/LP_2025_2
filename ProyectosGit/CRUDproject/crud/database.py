import sqlite3
conexion = sqlite3.connect("database.db")

query="""
CREATE TABLE if not exists contactos(
id INT PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
phone TEXT NOT NULL
);
"""
conexion.execute(query)
