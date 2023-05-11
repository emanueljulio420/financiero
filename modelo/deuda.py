class Deuda:
    def __init__(self, id, valor, fecha, descripcion, interes=0):
        self.id = id
        self.valor = valor
        self.fecha_inicio = fecha
        self.descripcion = descripcion
        self.interes = interes

    def __str__(self):
        return f"ID: {self.id}\nValor: {self.valor} \nFecha: {self.fecha_inicio}\nInteres: {self.interes} \nDescripcion: {self.descripcion}\n"
