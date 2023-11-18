import random

import reflex as rx


class State(rx.State):
    number: int = 0
    text = "Change Me!"
    selected: str = "DOGE"

    def update(self):
        self.number = random.randint(0, 100)

    def change_text(self, text):
        if self.text == "Change Me!":
            self.text = "Changed!"
        else:
            self.text = "Change Me!"
    
    pass



