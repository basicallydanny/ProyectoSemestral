import random

import reflex as rx

from ProyectoSemestral.state import State
from ProyectoSemestral.templates import template

lugares = ["Base", "Saman", "Boqueria", "Educon", "CDL", "Gorus", "Almendros","Guayacanes", "impresion","Cedro", "Palmas", "N/A"]

@template(route="/reservas", title="Reservas")
def reservas() -> rx.Component:
    return rx.vstack(
    rx.heading("SELECCIONE EL TIPO DE SERVICIO", font_size="2.5em", color="#808080", style={"margin-bottom": "20px"}),
    rx.divider(),
    rx.text("SELECCIONE EL LUGAR DE RECOGIDA", font_size="1em", color="#4682B4"),
    rx.select(
        lugares,
        value=State.lugar1,
        on_change=State.set_lugar1,
    ),
    rx.text("SELECCIONE EL LUGAR DE ENTREGA", font_size="1em", color="#4682B4"),
    rx.text("En caso de ser una grabación, seleccione N/A", font_size="0.9em", color="#4682B4"),
    rx.select(
        lugares,
        value=State.lugar2,
        on_change=State.set_lugar2,
    ),
    rx.hstack(
    rx.vstack(
    rx.input(
            placeholder="Peso (kg)",
            on_blur=State.weight,
    ),
    rx.cond(
            State.domicilio,
            rx.text("Servicio: Domicilio", color="blue"),
            rx.text("Servicio: Grabación", color="blue"),
    ),
    ),
    rx.form(
        rx.vstack(
            rx.input(
                placeholder="Codigo",
                id="codigo",
            ),
            rx.input(
                placeholder="Hora de Servicio",
                id="hora",
            ),
            rx.input(
                type_="date",
                id="fecha",
                placeholder="Fecha de Servicio"
            ),
            rx.button("Confirmar", type_="submit"),
        ),
        on_submit=State.handle_submit, # handle_submit se tendría que modificar para tomar todos los datos y ponerlos en una reserva / orden
    ),
    rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header("Confimado"),
                rx.modal_body(
                    "¡La reserva ha sido exitosa!"
                ),
                rx.modal_footer(
                    rx.button(
                        "Cerrar", on_click=State.change
                    )
                ),
            ),
        ),
        is_open= State.confirmado,
        ),
    ),
    #rx.text(f"El encargo será realizado en {State.lugar1}."),
    #rx.text(f"El encargo será entregado en {State.lugar2}."),
    #rx.text(State.form_data.to_string()),
)
