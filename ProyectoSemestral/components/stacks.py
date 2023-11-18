import reflex as rx

from ProyectoSemestral import styles
from ProyectoSemestral.state import State


def stacks(v: int) -> rx.Component:
    if v >= 50:
        color = "green"
    elif 0 < v and v > 10:
        color = "yellow"
    else:
        color = "red"
    label_text = f"{v}%"
    return rx.box(
        rx.circular_progress(
            rx.circular_progress_label(label_text, color=color),
            value=v,
            color=color
        )
    )

def stacks2(s: str) -> rx.Component:
    if s == "libre":
        color = "green"
    elif s == "ocupado":
        color = "blue"
    else:
        color = "yellow"
    return rx.box(
        rx.circular_progress(
            rx.circular_progress_label(s, color=color),
            color=color,
            is_indeterminate=True
        )
    )

