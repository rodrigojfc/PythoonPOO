from cuentabancaria import Cuenta_bancaria
class Cuentadeahorro(Cuenta_bancaria):
    def __init__ (self, nombrecliente, numerocuenta, cantidad):
        super().__init__(nombrecliente, numerocuenta, cantidad)