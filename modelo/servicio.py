class Servicio:
    def __init__(self, valor, nombre, id):
        self.id = id
        self.valor = valor
        self.nombre = nombre

    def __str__(self):
        return f"Id: {self.id}\nNombre: {self.nombre}\nValor: {self.valor}\n"