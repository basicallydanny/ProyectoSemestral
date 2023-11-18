from sys import stdin

import psycopg2
import reflex as rx

from ProyectoSemestral import styles  # state,
from ProyectoSemestral.pages import *

connection = None

try: #se conecta con la base de datos
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'juan2013',
        database = 'PostgreSQL 11',
        port = '5433'
    )
    print("Conexión exitosa")
except Exception as ex: print(ex)

#cursordb = connection.cursor() #cursor que hara todas las operaciones

#guardamos la fecha actual
#cursordb.execute("SELECT current_timestamp")
#fechahoy = cursordb.fetchone()[0]

def crearTablas():
        # Crear tabla Administrador
    cursordb.execute('''CREATE TABLE Administrador (
                        cedula INTEGER PRIMARY KEY,
                        nombre TEXT,
                        contraseña TEXT
                    )''')

    # Crear tabla Vehículo
    cursordb.execute('''CREATE TABLE Vehiculo (
                        placa TEXT PRIMARY KEY,
                        tipo TEXT,
                        bateria INTEGER,
                        distancia_total INTEGER,
                        estado TEXT
                    )''')

    # Crear tabla Viaje
    cursordb.execute('''CREATE TABLE Viaje (
                        Id SERIAL PRIMARY KEY,
                        lugar_salida TEXT,
                        lugar_llegada TEXT,
                        gasto_bateria INTEGER,
                        metros_recorridos INTEGER
                    )''')

    # Crear tabla Orden
    cursordb.execute('''CREATE TABLE Orden (
                        idorden SERIAL PRIMARY KEY,
                        lugar_recogida TEXT,
                        lugar_entrega TEXT
                    )''')

    # Crear tabla Reserva
    cursordb.execute('''CREATE TABLE Reserva (
                        idreserva SERIAL PRIMARY KEY,
                        idorden INTEGER references Orden(idorden),
                        hora_salida TIMESTAMP,
                        codigo_universitario_reserva TEXT,
                        placa TEXT references Vehiculo(placa),
                        cedula INTEGER references Administrador(cedula)
                    )''')
    
    # Crear tabla Viaje_orden
    cursordb.execute('''CREATE TABLE Viaje_orden (
                        Idorden INTEGER REFERENCES Orden(idorden),
                        id INTEGER REFERENCES Viaje(Id),
                        PRIMARY KEY(idorden,id)
                    )''')

def insertarDatos():#Crea datos iniciales
    cursordb.execute('''INSERT INTO VIAJE (lugar_salida, lugar_llegada, gasto_bateria, metros_recorridos) VALUES
                        ('Base', 'impresion', 1, 20),
                        ('Base', 'Gorus', 3, 55),
                        ('Base', 'Boqueria', 2, 40),
                        ('Base', 'Almendros', 3, 50),
                        ('Base', 'Saman', 2, 40),
                        ('Base', 'Guayacanes', 3, 50),
                        ('Base', 'Cedro', 5, 80),
                        ('Base', 'Palmas', 3, 50),
                        ('Base', 'impresion', 1, 20),
                        ('Base', 'Educon', 1, 30),
                        ('Base', 'CDL', 5, 90),
                 
                        ('impresion', 'Educon', 1, 30),
                        ('impresion', 'Palmas', 1, 30),
                        ('impresion', 'Saman', 2, 40),
                        ('impresion', 'Cedro', 5, 80),
                        ('impresion', 'Guayacanes', 3, 50),
                        ('impresion', 'Almendros', 2, 45),
                 
                        ('Boqueria', 'Educon', 2, 40),
                        ('Boqueria', 'Palmas', 1, 20),
                        ('Boqueria', 'Saman', 3, 50),
                        ('Boqueria', 'Cedro', 6, 100),
                        ('Boqueria', 'Guayacanes', 1, 30),
                        ('Boqueria', 'Almendros', 3, 50),
                 
                        ('Gorus', 'Educon', 1, 30),
                        ('Gorus', 'Palmas', 6, 100),
                        ('Gorus', 'Saman', 1, 30),
                        ('Gorus', 'Cedro', 3, 50),
                        ('Gorus', 'Guayacanes', 5, 90),
                        ('Gorus', 'Almendros', 1, 10);''')

    cursordb.execute('''INSERT INTO ADMINISTRADOR (cedula, nombre, contraseña) VALUES
                            (1007370990, 'Juan Cespedes', '12345'),
                            (1234567890, 'Juan Aguado', '54321'),
                            (0987654321, 'Daniela Gomez', '98765');''')

    cursordb.execute('''INSERT INTO VEHICULO (placa, tipo, bateria, distancia_total, estado) VALUES
                            ('ABC000', 'dron', 100, 500, 'ocupado'),
                            ('ABC001', 'dron', 100, 200, 'ocupado'),
                            ('ABC002', 'dron', 100, 350, 'libre'),
                            ('ABC003', 'dron', 100, 1045, 'mantenimiento'),
                            ('ABC004', 'dron', 100, 100, 'mantenimiento'),
                            ('CBA000', 'robot', 100, 1000, 'libre'),
                            ('CBA001', 'robot', 100, 600, 'ocupado'),
                            ('CBA002', 'robot', 100, 400, 'ocupado'),
                            ('CBA003', 'robot', 100, 330, 'mantenimiento'),
                            ('CBA004', 'robot', 100, 210, 'ocupado');''')

def vehiculos():# Obtener atributos de vehículos
    cursordb.execute('''SELECT placa, tipo, bateria, distancia_total, estado FROM Vehiculo''')
    robs = cursordb.fetchall()
    return robs

def reserva(id_reserva): #Obtener información de la reserva dado el ID
    cursordb.execute('''SELECT * FROM Reserva WHERE idreserva = %s''', (id_reserva,))
    reserva = cursordb.fetchone()
    return reserva

def reservar(id_reserva, id_orden, hora_salida, codigo_universitario, placa, cedula):
    cursordb.execute('''
        INSERT INTO Reserva (idreserva, idorden, hora_salida, codigo_universitario, placa, cedula)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (id_reserva, id_orden, hora_salida, codigo_universitario, placa, cedula))


app = rx.App(style=styles.base_style)
app.compile()

#connection.commit()
#cursordb.close()
#connection.close()
