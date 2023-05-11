
class Menu:

    def menu(self,u):
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