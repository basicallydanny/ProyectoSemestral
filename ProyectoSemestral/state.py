import random

import reflex as rx


class State(rx.State):
    pesoMax: int = 1.5
    peso: str = None
    lugar1: str = "Base"
    lugar2: str = "Saman"
    image_clicked: int = 0
    domicilio: True

    form_data: dict = {}

    def weight(self, pesoPedido: str):
        self.peso = int(pesoPedido)
        if self.peso > self.pesoMax:
            return
        

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        return [
            rx.set_value(field_id, "")
            for field_id in form_data
        ]
    
    pass



