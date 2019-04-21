from random import randint

# Classe que representa um unico dado

class Die():

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # Devolve um valor aleatorio entre 1 e 6
    def roll(self):
        return randint(1, self.num_sides)