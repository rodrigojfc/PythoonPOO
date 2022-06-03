class Cuenta_bancaria():
    def __init__ (self, nombrecliente, numerocuenta, cantidad): #parametros
        self.__nombrecliente = nombrecliente
        self.__numerocuenta = numerocuenta
        self.__cantidad = cantidad

    def agregar_fondos(self):
        x = int(input("Ingrese fondos a agregar $ "))
        self.__cantidad += x
        print(f'Los nuevos fondos son ${self.__cantidad}')
    
    def retirar(self):
        x = int(input("Cuanto quieres retirar? ") )
        if self.__cantidad <= x:
            print("no tienes fondos disponibles")
        else:
            self.__cantidad -= x
        print(f'Se ha retirado $ {x} , Nuevo saldo disponible $ {self.__cantidad} ')
    def Balance(self):
        print(f'Su balance actual es $ {self.__cantidad}')

