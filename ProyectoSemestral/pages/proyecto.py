import reflex as rx

from ProyectoSemestral import styles
from ProyectoSemestral.templates import template


@template(route="/proyecto", title="Proyecto")
def proyecto() -> rx.Component:
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
