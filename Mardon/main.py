from cuentabancaria import Cuenta_bancaria 
from cuentadeahorro import Cuentadeahorro

cuenta1 = Cuenta_bancaria ("Mardon", 12345, 50)
cuenta2 = Cuentadeahorro("Mardon", 54321, 50, 12)



def premenu():
    x= int(input(" Que tipo de cuenta posee con nosotros? \n1-para Cuenta Corriente\n2- para Cuenta de Ahorros \n"))
    if x ==1:    
        print("Ha seleccionado Cuenta Corriente")
        menu1(cuenta1, 1)
    elif x ==2: 
        print("Ha seleccionado Cuenta de ahorro")
        menu1(cuenta2, 2)
    else:
        print("Ha introducido una opcion equivocada")


def menu1(objeto, select):
    x = 0
    while x != 6 :
        print("Elija su opcion: \n")
        print("Opcion 1 - Agregar fondos \n")
        print("Opcion 2 - Retirar fondos\n")
        print("Opcion 3 - Balance de cuenta \n")
        if select == 2:
            print("Opcion 4 - Ver plazo actual de cuenta\n")
            print("Opcion 5 - Modificar plazo")
            print("Opcion 6 - Salir")
        else:
            print("Opcion 6 - Salir \n")

        x=int(input ("Ingrese numero de opcion \n"))
        if x == 1:
            objeto.agregar_fondos()
        elif x ==2:
            objeto.retirar()
        elif x ==3:
            objeto.Balance()
        elif x == 4:
            objeto.verPlazo()
        elif x == 5:
            objeto.cambioPlazo()
        
premenu()





