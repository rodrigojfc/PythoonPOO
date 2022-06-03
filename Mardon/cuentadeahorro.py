from cuentabancaria import Cuenta_bancaria

class Cuentadeahorro(Cuenta_bancaria):
    def __init__ (self, nombrecliente, numerocuenta, cantidad, plazo):
        super().__init__(nombrecliente, numerocuenta, cantidad)
        self.__plazo = plazo


    def cambioPlazo(self):

        nuevoplazo = int(input("Ingrese el nuevo plazo: "))
        self.__plazo = nuevoplazo

        print(f'El nuevo plazo es: {self.__plazo}')
    
    def verPlazo(self):

        print(f'El plazo actual es: {self.__plazo}')