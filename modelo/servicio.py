class Servicio:
    def __init__(self, valor, nombre):
        self.valor = valor
        self.nombre = nombre

    def __str__(self):
        return f"Nombre {self.nombre} Valor {self.valor}\n"