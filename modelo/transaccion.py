class Transaccion:
    def __init__(self, id, fecha, valor, descripcion):
        self.id = id
        self.fecha = fecha
        self.valor = valor
        self.descripcion = descripcion

    def __str__(self):
        return f"Fecha {self.fecha}\n Valor {self.valor}\n Descripcion{self.descripcion}\n"
