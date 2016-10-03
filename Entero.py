# CLASS ENTERO
class Entero:
    def __init__(self, ent):
        self.entero = ent # Expresion entera (str)
        self.e = int(self.entero) # Entero (int)

    def __str__(self):
        return str(self.entero)