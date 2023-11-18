import random

import reflex as rx


class State(rx.State):
    pesoMax: int = 1.5
    peso: str = None
    lugar1: str = "Base"
    lugar2: str = "Saman"
    image_clicked: int = 0
    domicilio: bool = True
    confirmado: bool = False
    form_data: dict = {}

    def weight(self, pesoPedido: str):
        if pesoPedido != "N/A":
            self.domicilio = True
            self.peso = int(pesoPedido)
            if self.peso > self.pesoMax:
                return rx.window_alert("El peso registrado supera el máximo peso soportado.")
        else:
            self.domicilio = False
    
    def change(self):
        self.confirmado = not (self.confirmado)

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.change() #muestra mensaje que se completó exitosamente
        return [
            rx.set_value(field_id, "")
            for field_id in form_data
        ]
        
    
    pass



