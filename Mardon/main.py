from cuentabancaria import Cuenta_bancaria 
from cuentadeahorro import Cuentadeahorro

cuenta1 = Cuenta_bancaria ("Mardon", 12345, 50 )
cuenta2 = Cuentadeahorro("Mardon", 54321, 50)

x= int(input(" Que tipo de cuenta posee con nosotros? Presione 1 para Cuenta Corriente o 2 para Cuenta de Ahorros \n"))
if x ==1:    
    print("Ha seleccionado Cuenta Corriente")
elif x ==2: 
        print("Ha seleccionado cuenta de ahorro")

def menu1():
    x = 0
    while x != 4 :
        print("Elija su opcion: \n")
        print("Opcion 1 - Agregar fondos \n")
        print("Opcion 2 - Retirar fondos\n")
        print("Opcion 3 - Balance de cuenta \n")
        print("Opcion 4 - Salir \n")
        x=int(input ("Ingrese numero de opcion \n"))
        if x == 1:
            cuenta1.agregar_fondos()
        elif x ==2:
            cuenta1.retirar()
        elif x ==3:
            cuenta1.Balance()
def menu2():
    x = 0
while x != 4 :
        print("Elija su opcion: \n")
        print("Opcion 1 - Agregar fondos \n")
        print("Opcion 2 - Retirar fondos\n")
        print("Opcion 3 - Balance de cuenta \n")
        print("Opcion 4 - Salir \n")
        x=int(input ("Ingrese numero de opcion \n"))
        if x == 1:
            cuenta1.agregar_fondos()
        elif x ==2:
            cuenta1.retirar()
        elif x ==3:
            cuenta1.Balance()

if x == 1:
    menu()
if x ==2:
    menu2()