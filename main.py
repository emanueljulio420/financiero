import datetime

class Deuda:
    def __init__(self, id, valor, fecha, descripcion, interes=0):
        self.id = id
        self.valor = valor
        self.fecha_inicio = fecha
        self.descripcion = descripcion
        self.interes = interes

    def __str__(self):
        return f"Valor de la deuda es de {self.valor} \nfecha de inicio {self.fecha_inicio}\nInteres del {self.interes} \nDescripcion {self.descripcion}"

class Transaccion:
    def __init__(self, id, fecha, valor, descripcion):
        self.id = id
        self.fecha = fecha
        self.valor = valor
        self.descripcion = descripcion

    def __str__(self):
        return f"Fecha {self.fecha}\n Valor {self.valor}\n Descripcion{self.descripcion}"

class Servicio:
    def __init__(self, valor, nombre):
        self.valor = valor
        self.nombre = nombre

    def __str__(self):
        return f"Nombre {self.nombre} Valor {self.valor}"


class Usuario:
    def __init__(self, nombre, cedula, saldo):
        self.nombre = nombre
        self.deudas = []
        self.servicios = []
        self.transacciones = []
        self.cedula = cedula
        self.saldo = saldo
    def pagar_deuda(self, id):
        for i in self.deudas:
            if i.id == id:
                if i.valor > self.saldo:
                    print("Saldo insuficiente")
                    break
                self.saldo -= i.valor
                new_transaccion = Transaccion(len(self.transacciones) + 1, datetime.datetime.now().date(), i.valor,
                                              i.descripcion)
                self.transacciones.append(new_transaccion)
                print("Deuda pagado")
    def agregar_deuda(self):
        valor = int(input("Ingrese el valor del servicio: "))
        descripcion = int(input("Ingrese el nombre del servicio: "))
        fecha_inicio = datetime.datetime.now().date()
        id = len(self.deudas) + 1
        interes = int(input("Ingrese el porcentaje del interes: "))
        new_deuda = Deuda(id, valor, fecha_inicio, descripcion, interes)
        self.servicios.append(new_deuda)
        print("Deuda agregada con éxito!!!!")

    def verDeudas(self):
        if self.deudas == []:
            print('No tienes deudas')
        else:
            for deudas in self.deudas:
                print(deudas)
    def agregar_servicio(self):
        valor = int(input("Ingrese el valor del servicio: "))
        nombre = int(input("Ingrese el nombre del servicio: "))
        new_servicio = Servicio(valor, nombre)
        self.servicios.append(new_servicio)
        print("Servicio agregado con éxito!!!!")

    def pagar_servicio(self):
        for i in self.servicios:
            if i.id == id:
                if i.valor > self.saldo:
                    print("Saldo insuficiente")
                    break
                self.saldo -= i.valor
                new_transaccion = Transaccion(len(self.transacciones) + 1, datetime.datetime.now().date(), i.valor,
                                              i.nombre)
                self.transacciones.append(new_transaccion)
                print("Deuda pagado")

    def verServicios(self):
        for servicio in self.servicios:
            print(servicio)

    def verTransacciones(self):
        for transeccion in self.transacciones:
            print(transeccion)



u = Usuario('Pepe',12,12000)

while True:
    print('--------------  Gestor financiero  ----------------')
    print('1. Ver deudas')
    print('2. Agregar deuda')
    print('3. Pagar deuda')
    print('4. Agregar servicio')
    print('5. pagar servicio')
    opc = input('Ingrese la accion que desea realizar: ')

    if (opc == 1):
        u.verDeudas()

    if (opc == 2):
        u.agregar_deuda()