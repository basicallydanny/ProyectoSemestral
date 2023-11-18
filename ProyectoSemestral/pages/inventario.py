import reflex as rx

from ProyectoSemestral.components.stacks import stacks, stacks2
from ProyectoSemestral.templates import template

number = 1
distancia = 3
roboID = f"ID 0{number}"
tDistance = f"{distancia} km"

@template(route="/inventario", title="Inventario")
def inventario() -> rx.Component:
    return rx.vstack(
        rx.heading("Inventario", font_size="3em", style={"margin-bottom": "30px"}),

        rx.vstack(  # ROBOT #1
            rx.hstack(
                rx.heading(roboID, size="xl", color="#4682B4", style={"margin-right": "40px"}),
                rx.image(src="/robot.png", width="100px", height="auto"),
                rx.stack(  # Bateria
                    rx.text("Bateria", size="0.2em", color="#808080"),
                    stacks(5),
                    direction="column",
                    style={"margin-right": "50px"}
                ),
                rx.stack(  # Distancia Total
                    rx.text("Distancia Total", size="0.2em", color="#808080"),
                    rx.text(tDistance, size="10px", as_="b"),
                    direction="column"
                ),
            ),

            rx.hstack(
                rx.stack(  # Estado
                    rx.text("Estado", size="0.2em", color="#808080"),
                    stacks2("libre"),
                    direction="column",
                    style={"margin-left": "210px"}
                ),
                rx.stack(  # Recorrido
                    rx.text("Recorrido", size="0.2em", color="#808080"),
                    rx.button("Seguir", variant="ghost"),
                    direction="column",
                    style={"border-radius": "xl", "width": "100%"}
                ),
            ),
            
            rx.hstack(
                rx.avatar(size="md"),
                rx.stack( # Persona
                    rx.text("Información de Reserva", size="0.02em", color="#808080"),
                    rx.text("Nombre Apellido", size="3em", color="back", as_="b", style={"margin-right": "70px"}),
                    direction="column",
                ),
            ),
            style={"border-radius": "xl", "width": "100%", "padding": "60px", "background-color": "#f5f5f5", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
        ),

        rx.spacer(),

        rx.vstack(  # ROBOT #2
            rx.hstack(
                rx.heading(roboID, size="xl", color="#4682B4", style={"margin-right": "40px"}),
                rx.image(src="/robot.png", width="100px", height="auto"),
                rx.stack(  # Bateria
                    rx.text("Bateria", size="0.2em", color="#808080"),
                    stacks(70),
                    direction="column",
                    style={"margin-right": "50px"}
                ),
                rx.stack(  # Distancia Total
                    rx.text("Distancia Total", size="0.2em", color="#808080"),
                    rx.text(tDistance, size="10px", as_="b"),
                    direction="column"
                ),
            ),

            rx.hstack(
                rx.stack(  # Estado
                    rx.text("Estado", size="0.2em", color="#808080"),
                    stacks2("mantenimiento"),
                    direction="column",
                    style={"margin-left": "210px"}
                ),
                rx.stack(  # Recorrido
                    rx.text("Recorrido", size="0.2em", color="#808080"),
                    rx.button("Seguir", variant="ghost"),
                    direction="column",
                    style={"border-radius": "xl", "width": "100%"}
                ),
            ),
            
            rx.hstack(
                rx.avatar(size="md"),
                rx.stack( # Persona
                    rx.text("Información de Reserva", size="0.02em", color="#808080"),
                    rx.text("Nombre Apellido", size="3em", color="back", as_="b", style={"margin-right": "70px"}),
                    direction="column",
                ),
            ),
            style={"border-radius": "xl", "width": "100%", "padding": "60px", "background-color": "#f5f5f5", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
        ),

        rx.spacer(),

        rx.vstack(  # ROBOT #3
            rx.hstack(
                rx.heading(roboID, size="xl", color="#4682B4", style={"margin-right": "40px"}),
                rx.image(src="/robot.png", width="100px", height="auto"),
                rx.stack(  # Bateria
                    rx.text("Bateria", size="0.2em", color="#808080"),
                    stacks(35),
                    direction="column",
                    style={"margin-right": "50px"}
                ),
                rx.stack(  # Distancia Total
                    rx.text("Distancia Total", size="0.2em", color="#808080"),
                    rx.text(tDistance, size="10px", as_="b"),
                    direction="column"
                ),
            ),

            rx.hstack(
                rx.stack(  # Estado
                    rx.text("Estado", size="0.2em", color="#808080"),
                    stacks2("ocupado"),
                    direction="column",
                    style={"margin-left": "210px"}
                ),
                rx.stack(  # Recorrido
                    rx.text("Recorrido", size="0.2em", color="#808080"),
                    rx.button("Seguir", variant="ghost"),
                    direction="column",
                    style={"border-radius": "xl", "width": "100%"}
                ),
            ),
            
            rx.hstack(
                rx.avatar(size="md"),
                rx.stack( # Persona
                    rx.text("Información de Reserva", size="0.02em", color="#808080"),
                    rx.text("Nombre Apellido", size="3em", color="back", as_="b", style={"margin-right": "70px"}),
                    direction="column",
                ),
            ),
            style={"border-radius": "xl", "width": "100%", "padding": "60px", "background-color": "#f5f5f5", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
        ),

        rx.spacer(),

        rx.vstack(  # DRON #1
            rx.hstack(
                rx.heading(roboID, size="xl", color="#4682B4", style={"margin-right": "40px"}),
                rx.image(src="/dron.png", width="100px", height="auto"),
                rx.stack(  # Bateria
                    rx.text("Bateria", size="0.2em", color="#808080"),
                    stacks(5),
                    direction="column",
                    style={"margin-right": "50px"}
                ),
                rx.stack(  # Distancia Total
                    rx.text("Distancia Total", size="0.2em", color="#808080"),
                    rx.text(tDistance, size="10px", as_="b"),
                    direction="column"
                ),
            ),

            rx.hstack(
                rx.stack(  # Estado
                    rx.text("Estado", size="0.2em", color="#808080"),
                    stacks2("libre"),
                    direction="column",
                    style={"margin-left": "210px"}
                ),
                rx.stack(  # Recorrido
                    rx.text("Recorrido", size="0.2em", color="#808080"),
                    rx.button("Seguir", variant="ghost"),
                    direction="column",
                    style={"border-radius": "xl", "width": "100%"}
                ),
            ),
            
            rx.hstack(
                rx.avatar(size="md"),
                rx.stack( # Persona
                    rx.text("Información de Reserva", size="0.02em", color="#808080"),
                    rx.text("Nombre Apellido", size="3em", color="back", as_="b", style={"margin-right": "70px"}),
                    direction="column",
                ),
            ),
            style={"border-radius": "xl", "width": "100%", "padding": "60px", "background-color": "#f5f5f5", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
        ),

        rx.spacer(),

        rx.vstack(  # DRON #2
            rx.hstack(
                rx.heading(roboID, size="xl", color="#4682B4", style={"margin-right": "40px"}),
                rx.image(src="/dron.png", width="100px", height="auto"),
                rx.stack(  # Bateria
                    rx.text("Bateria", size="0.2em", color="#808080"),
                    stacks(70),
                    direction="column",
                    style={"margin-right": "50px"}
                ),
                rx.stack(  # Distancia Total
                    rx.text("Distancia Total", size="0.2em", color="#808080"),
                    rx.text(tDistance, size="10px", as_="b"),
                    direction="column"
                ),
            ),

            rx.hstack(
                rx.stack(  # Estado
                    rx.text("Estado", size="0.2em", color="#808080"),
                    stacks2("mantenimiento"),
                    direction="column",
                    style={"margin-left": "210px"}
                ),
                rx.stack(  # Recorrido
                    rx.text("Recorrido", size="0.2em", color="#808080"),
                    rx.button("Seguir", variant="ghost"),
                    direction="column",
                    style={"border-radius": "xl", "width": "100%"}
                ),
            ),
            
            rx.hstack(
                rx.avatar(size="md"),
                rx.stack( # Persona
                    rx.text("Información de Reserva", size="0.02em", color="#808080"),
                    rx.text("Nombre Apellido", size="3em", color="back", as_="b", style={"margin-right": "70px"}),
                    direction="column",
                ),
            ),
            style={"border-radius": "xl", "width": "100%", "padding": "60px", "background-color": "#f5f5f5", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
        ),

        rx.spacer(),

        rx.vstack(  # DRON #3
            rx.hstack(
                rx.heading(roboID, size="xl", color="#4682B4", style={"margin-right": "40px"}),
                rx.image(src="/dron.png", width="100px", height="auto"),
                rx.stack(  # Bateria
                    rx.text("Bateria", size="0.2em", color="#808080"),
                    stacks(35),
                    direction="column",
                    style={"margin-right": "50px"}
                ),
                rx.stack(  # Distancia Total
                    rx.text("Distancia Total", size="0.2em", color="#808080"),
                    rx.text(tDistance, size="10px", as_="b"),
                    direction="column"
                ),
            ),

            rx.hstack(
                rx.stack(  # Estado
                    rx.text("Estado", size="0.2em", color="#808080"),
                    stacks2("ocupado"),
                    direction="column",
                    style={"margin-left": "210px"}
                ),
                rx.stack(  # Recorrido
                    rx.text("Recorrido", size="0.2em", color="#808080"),
                    rx.button("Seguir", variant="ghost"),
                    direction="column",
                    style={"border-radius": "xl", "width": "100%"}
                ),
            ),
            
            rx.hstack(
                rx.avatar(size="md"),
                rx.stack( # Persona
                    rx.text("Información de Reserva", size="0.02em", color="#808080"),
                    rx.text("Nombre Apellido", size="3em", color="back", as_="b", style={"margin-right": "70px"}),
                    direction="column",
                ),
            ),
            style={"border-radius": "xl", "width": "100%", "padding": "60px", "background-color": "#f5f5f5", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
        ),

    )
