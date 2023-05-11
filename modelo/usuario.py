import datetime

from modelo.deuda import Deuda
from modelo.servicio import Servicio
from modelo.transaccion import Transaccion


class Usuario:
    def __init__(self, nombre, cedula, saldo):
        self.nombre = nombre
        self.deudas = []
        self.servicios = []
        self.transacciones = []
        self.cedula = cedula
        self.saldo = saldo

    def agreagarSaldo(self):
        print('\n')
        saldo = float(input('Ingrese saldo a agregar: '))
        self.saldo = self.saldo + saldo
        new_transaccion = Transaccion(len(self.transacciones) + 1, datetime.datetime.now().date(), saldo, 'Ingresos')
        self.transacciones.append(new_transaccion)
        print('Saldo agregado correctamente')
        print('\n')


    def pagar_deuda(self):
        self.verDeudas()
        if self.deudas == []:
            return
        else:
            id = int(input('Ingrese el id de la deuda: '))
            for i in self.deudas:
                if i.id == id:
                    if i.valor > self.saldo:
                        print("Saldo insuficiente")
                        break
                    self.saldo -= i.valor
                    new_transaccion = Transaccion(len(self.transacciones) + 1, datetime.datetime.now().date(), -i.valor,
                                                  i.descripcion)
                    self.transacciones.append(new_transaccion)
                    self.deudas.pop(id-1)
                    self.deudas.insert(id-1,0)
                    print("Deuda pagada")
    def agregar_deuda(self):
        print('\n')
        valor = int(input("Ingrese el valor de la deuda: "))
        descripcion = input("Ingrese descripcion de la deuda: ")
        fecha_inicio = datetime.datetime.now().date()
        id = len(self.deudas) + 1
        interes = int(input("Ingrese el porcentaje del interes: "))
        new_deuda = Deuda(id, valor, fecha_inicio, descripcion, interes)
        self.deudas.append(new_deuda)
        print("Deuda agregada con éxito!!!!")
        print('\n')

    def verDeudas(self):
        print('\n')
        if self.deudas == []:
            print('No tienes deudas')
        else:
            for deudas in self.deudas:
                if deudas != 0:
                    print(deudas)
        print('\n')
    def agregar_servicio(self):
        print('\n')
        valor = int(input("Ingrese el valor del servicio: "))
        nombre = input("Ingrese el nombre del servicio: ")
        new_servicio = Servicio(valor, nombre, len(self.servicios) + 1)
        self.servicios.append(new_servicio)
        print("Servicio agregado con éxito!!!!")
        print('\n')

    def pagar_servicio(self):
        self.verServicios()
        if self.servicios == []:
            return
        else:
            id = int(input('Ingrese el id del servicio: '))
            for i in self.servicios:
                if i.id == id:
                    if i.valor > self.saldo:
                        print("Saldo insuficiente")
                        break
                    self.saldo -= i.valor
                    new_transaccion = Transaccion(len(self.transacciones) + 1, datetime.datetime.now().date(), -i.valor,
                                                  i.nombre)
                    self.transacciones.append(new_transaccion)
                    self.servicios.pop(id-1)
                    self.deudas.insert(id-1,0)
                    print("Servicio pagado")
        print('\n')

    def verServicios(self):
        print('\n')
        if self.servicios == []:
            print('No tienes ningun servicio')
        else:
            for servicio in self.servicios:
                if servicio != 0:
                    print(servicio)
        print('\n')

    def verTransacciones(self):
        print('\n')
        if self.transacciones == []:
            print('No tienes ninguna transaccion realizada')
        else:
            for transeccion in self.transacciones:
                print(transeccion)
        print('\n')
