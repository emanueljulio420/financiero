class Deuda:
    def __init__(self, id, valor, fecha, descripcion, interes=0):
        self.id = id
        self.valor = valor
        self.fecha_inicio = fecha
        self.descripcion = descripcion
        self.interes = interes

    def __str__(self):
        return f"Numero de la deuda {self.id}\nValor de la deuda es de {self.valor} \nfecha de inicio {self.fecha_inicio}\nInteres del {self.interes} \nDescripcion {self.descripcion}\n"
