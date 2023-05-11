import datetime

class Deuda:
    def __init__(self, id, valor, fecha, descripcion, interes=0):
        self.id = id
        self.valor = valor
        self.fecha_inicio = fecha
        self.descripcion = descripcion
        self.interes = interes

    def __str__(self):
        return f"Numero de la deuda {self.id}\nValor de la deuda es de {self.valor} \nfecha de inicio {self.fecha_inicio}\nInteres del {self.interes} \nDescripcion {self.descripcion}\n"

class Transaccion:
    def __init__(self, id, fecha, valor, descripcion):
        self.id = id
        self.fecha = fecha
        self.valor = valor
        self.descripcion = descripcion

    def __str__(self):
        return f"Fecha {self.fecha}\n Valor {self.valor}\n Descripcion{self.descripcion}\n"

class Servicio:
    def __init__(self, valor, nombre):
        self.valor = valor
        self.nombre = nombre

    def __str__(self):
        return f"Nombre {self.nombre} Valor {self.valor}\n"


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
        new_servicio = Servicio(valor, nombre)
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
class Menu:

    def menu(self):
        u = Usuario('Pepe',12,12000)
        while True:
            print('--------------  Gestor financiero  ----------------')
            print('1. Agreagar saldo')
            print('2. Ver deudas')
            print('3. Agregar deuda')
            print('4. Pagar deuda')
            print('5. Ver servicios')
            print('6. Agregar servicio')
            print('7. Pagar servicio')
            print('8. Ver transacciones')
            opc = int(input('Ingrese la accion que desea realizar: '))

            if (opc == 1):
                u.agreagarSaldo()

            if (opc == 2):
                u.verDeudas()

            if (opc == 3):
                u.agregar_deuda()

            if (opc == 4):
                u.pagar_deuda()

            if (opc == 5):
                u.verServicios()

            if (opc == 6):
                u.agregar_servicio()

            if (opc == 7):
                u.pagar_servicio()

            if (opc == 8):
                u.verTransacciones()


m = Menu()
m.menu()