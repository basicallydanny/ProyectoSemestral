import datetime
import requests
import reflex as rx

from ProyectoSemestral import styles
from ProyectoSemestral.templates import template

log_data = ["Message 1", "Message 2", "Message 3"]
#En esta lista se pueden guardar toda la información con respecto
#a las entregas. Por ende, habría una función que llene la lista log_data.

def fechaHora():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%A, %d de %B de %Y")
    formatted_time = now.strftime("%H:%M:%S")
    return f"Fecha: {formatted_date}, Hora: {formatted_time}"

def dateTime() -> rx.Component:
    return rx.text(fechaHora(), font_size="1em", color = "#808080")

@template(route="/", title="Menu", image= "menu.png")
def index() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # USUARIO CONECTADO
            rx.avatar(
                rx.avatar_badge(
                    box_size="1.25em",
                    bg="green.500",
                    border_color="green.500",
                ),
                name="Juan Cespedes",
            ),
            rx.spacer(),
            rx.text("Juan Cespedes", font_size="0.8em", color="#808080", as_="b"),
        ),
        dateTime(),
        rx.spacer(),
        rx.hstack(
            # LO DEL CLIMA
            # Solo se pone que retorne la información como si fuera un print
            # Supongamos que A tiene el texto que queremos mostrar:
            # rx.text(A, font_size="1.5em", color = "#4682B4")
        ),
        rx.vstack(
            # BOTONES
            rx.link(
                rx.button("Registrar Solicitud"),
                href="/reservas",
                color="rgb(107,99,246)",
                button=True,
            ),
            rx.link(
                rx.button("Inventario"),
                href="/inventario",
                color="rgb(107,99,246)",
                button=True,
            ),
        ),
        rx.spacer(),
        rx.spacer(),
        rx.heading("BITÁCORA DE SERVICIOS", font_size="2.5em", color="#808080", style={"margin-bottom": "20px"}),
        rx.list(
                items= log_data,
                spacing=".25em",
        )
    )

def obtener_clima(api_key, ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        clima = datos['main']['temp']
        condiciones_clima = datos['weather'][0]['description']
        print(f"La temperatura en {ciudad} es: {clima} grados Celsius")
        print(f"Condiciones climáticas: {condiciones_clima}")

        # Verificar si está lloviendo
        if 'rain' in condiciones_clima.lower():
            print("¡Está lloviendo! No se recomienda volar el dron.")
        else:
            print("Las condiciones son adecuadas para volar el dron.")
    else:
        print(f"No se pudo obtener el clima. Código de estado: {respuesta.status_code}")
        print(datos)

if __name__ == "__main__":
    api_key = 'b43ebcfbc020e122e8a0b04c1006f1e5'
    ciudad = input("Ingrese el nombre de la ciudad: ")
    obtener_clima(api_key, ciudad)