import random

import reflex as rx

from ProyectoSemestral.state import State
from ProyectoSemestral.templates import template

coins = ["BTC", "ETH", "LTC", "DOGE"]

@template(route="/reservas", title="Reservas")
def reservas() -> rx.Component:
    return rx.vstack(
        rx.text(
            f"The number is {State.number}"
        ),
        rx.button(
            "Update Number",
            on_click = State.update(),
        ),
        rx.input(
            value=State.text, on_focus=State.change_text
        ),

        # Using a var operation to concatenate a string with a var.
        rx.heading(
            "I just bought a bunch of "
            + State.selected
        ),
        # Using an f-string to interpolate a var.
        rx.text(
            f"{State.selected} is going to the moon!"
        ),
        rx.select(
            coins,
            value= State.selected,
            on_change=State.set_selected,
        ),
    )