from cProfile import label
from cgitb import text

from tkinter import *
from tkinter import messagebox
# ttk nos permitira crear la tablade nuestra BD
from tkinter import ttk
import sqlite3

from tkinter.tix import Tree

# Creación de la interfaz grafica
ventana =Tk()
ventana.title("App CRUD con Base de Datos")
ventana.geometry("600x350")

Id = StringVar()
Nombre = StringVar()
Cargo = StringVar()
Salario = StringVar()

def conexionBD():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE empleado (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(50) NOT NULL,
            CARGO VARCHAR(50) NOT NULL,
            SALARIO INT NOT NULL) 
        ''')
        messagebox.showinfo("CONEXION","Base de Datos Creada Exitoamente!")
    except:
        messagebox.showinfo("CONEXION","Conexion exitosa con la Base de Datos!")

def eliminarBD():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    if messagebox.askyesno(message="Los datos se perderan definitivamente, desea continuar la eliminacion?", title= "ADVERTENCIA"):
        miCursor.execute("DROP TABLE empleado")
    else:
        pass

def salirAplicacion():
    valor = messagebox.askquestion("SALIR","Esta seguro que desea salir de la APP?")
    if valor == "yes":
        ventana.destroy()

def limpiarCampos():
    Id.set("")
    Nombre.set("")
    Cargo.set("")
    Salario.set("")

def mensaje():
    acerca = '''
    APP CRUD
    Version 1.0
    Tecnologia Tkinter Python'''

############### Creacion del CRUD ############### 

def crear():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    try:
        datos = Nombre.get(), Cargo.get(), Salario.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)",(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al crear el registro, verificar la conexion con la BD")
        pass
    limpiarCampos()
    mostrar()

def mostrar():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    registros = Tree.get_children()
    for elementos in registros:
        Tree.delete(elementos)
    try:
        miCursor.execute("SELECT * FROM empleado")
        miConexion.commit()
        for row in miCursor:
            Tree.insert("", 0, text = row[0], values = (row[1],row[2],row[3]))
    except:
        pass

def actualizar():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    try:
        datos = Nombre.get(), Cargo.get(), Salario.get()
        miCursor.execute("UPDATE empleado SET Nombre=?, Cargo=?, Salario=? WHERE Id="+ Id.get(), (datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al actualizar el registro")
        pass
    limpiarCampos()
    mostrar()

def borrar():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    try:
        if messagebox.askyesno(message="Realmente desea eliminar el registro?", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM empleado WHERE Id="+ Id.get())
            miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al tratar de eliminar el registro")
        pass
    limpiarCampos()
    mostrar()

############### Tabla ###############
 
Tree = ttk.Treeview(height = 10, columns = ('#0', '#1', '#2'))
Tree.place(x = 0, y = 130)

Tree.column('#0', width= 100)
Tree.heading('#0', text = "ID", anchor = CENTER)
Tree.heading('#1', text = "Nombre Empleado", anchor = CENTER)
Tree.heading('#2', text = "Cargo", anchor = CENTER)
Tree.column('#3', width= 100)
Tree.heading('#3', text = "Salario", anchor = CENTER)

def seleccionarUsandoClick(event):
    item=Tree.identify('item', event.x, event.y)
    Id.set(Tree.item(item, "text"))
    Nombre.set(Tree.item(item, "values")[0])
    Cargo.set(Tree.item(item, "values")[1])
    Salario.set(Tree.item(item, "values")[2])

Tree.bind("<Double-1>", seleccionarUsandoClick)


############### Crear la ventana con sus elementos ###############

# Creacion de Menus
barraMenu = Menu(ventana)
estructuraMenu = Menu(barraMenu, tearoff=0)
estructuraMenu.add_command(label = "Crear/Conectar a BD", command = conexionBD)
estructuraMenu.add_command(label = "Eliminar BD", command = eliminarBD)
estructuraMenu.add_command(label = "Salir", command = salirAplicacion)
# Vincular a la barra de menu
barraMenu.add_cascade(label = "Inicio", menu = estructuraMenu)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label = "Limpiar Campos", command = limpiarCampos)
ayudaMenu.add_command(label = "Acerca de la APP", command = mensaje)
# Vincular a la barra de menu
barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)

# Creacion de etiquetas y cajas de texto
# Elementos de entrada

'''La siguiente variable creada tendra el Id de cada reguistro, no se mostrara es decir sera una variable oculta que 
el usuario no vera pero si nos funcionara para recolectar todos los valores del registro cuando vaya a ser creado, 
actualizado o eliminado'''
e1 = Entry(ventana, textvariable = Id)

# Creacion de etiquetas y cuadros de textos
l2 = Label(ventana, text="Nombre")
l2.place(x=30, y=10)
e2 = Entry(ventana, textvariable = Nombre, width = 50)
e2.place(x=100, y=10)

l3 = Label(ventana, text="Cargo")
l3.place(x=50, y=40)
e3 = Entry(ventana, textvariable = Cargo)
e3.place(x=100, y=40)

l4 = Label(ventana, text="Salario")
l4.place(x=280, y=40)
e4 = Entry(ventana, textvariable = Salario, width = 10)
e4.place(x=340, y=40)

l5 = Label(ventana, text="USD")
l5.place(x=400, y=40)

# Creacion de Botones

b1 = Button(ventana, text = "Crear Registro", bg = 'yellow', command = crear)
b1.place(x=50, y=90)
b2 = Button(ventana, text = "Modificar Registro", bg = 'yellow', command = actualizar)
b2.place(x=160, y=90)
b3 = Button(ventana, text = "Mostrar Registro", bg = 'yellow', command = mostrar)
b3.place(x=300, y=90)
b4 = Button(ventana, text = "Eliminar Registro", bg = 'red', command = borrar)
b4.place(x=430, y=90)

ventana.config(menu = barraMenu)

ventana.mainloop()