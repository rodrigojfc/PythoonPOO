class cuentanueva:
    import random
    cuentanueva = random.randint(1,99)
    def __init__(self, numerodecuenta, nombre, cantidad):
        self.__numerocuenta = numerodecuenta
        self.__nombre = nombre
        self.__cantidad = cantidad
    def numerodecuenta(self):
        x = int(input("Ingrese su numero de cuenta"))
        self.__numerocuenta = cuentanueva
        print(f'Su numero de cuenta es: {self.__numerocuenta}')  