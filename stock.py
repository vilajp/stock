"""""class OpenFiles():
    def __init__(self):
        self.files = []

    def open(self, *args):
        f = open(*args)
        self.files.append(f)
        return f

    def close(self):
        list(map(lambda f: f.close(), self.files))


files = OpenFiles()

# use open method
foo = files.open("text.txt", "r")

# close all files
files.close()

#############################################################################

def say_hello(name):
    print 'Hello {}!'.format(name)

# get the function by name
method_name = 'say_hello'
method = eval(method_name)

# call it like a regular function later
args = ['friend']
kwargs = {}
method(*args, **kwargs)

"""""

import os

class Archivo:
    #Los archivos van a ser clientes, proveedores y articulos
    def abrir(self, nombre, codigo="r"):
        archivo = open(nombre, codigo)
        return archivo
    
    def escribo(self, nombre, linea):
        archivo = write(linea)
        return
    
    def cerrar(self, archivo):
        archivo.close()
        return

class Persona:
    apellido=""
    nombre=""
    codigo=0
    direccion=""
    telefono=""


class Articulo:
    codigoBarras=""
    codigoInt="" # maximo numero en el archivo
    descripcion=""
    proveedor=""

    def movimientos(self, codigo):
        panta = Pantalla()
        panta.borrarPantalla()
        panta.mostrar("", "****Menu de Articulos****")

        if codigo == "01":
            panta.mostrar("", "******Altas******")
            linea = []

            codigoBarras = panta.pedir("Codigo de Barras:")
            while codigoBarras == "" or len(codigoBarras!=13):
                codigoBarras = panta.pedir("Ingrese de nuevo!, no puede estar vacio y ser menos de 13: ")

            codigoInt = panta.pedir("Codigo Interno:")
            while codigoInt == "" or len(codigoInt!=6):
                codigoInt = panta.pedir("Ingrese de nuevo!, no puede estar vacio y ser menos de 6: ")

            descripcion = panta.pedir("Ingrese una descripcion:")
            while descripcion == "":
                descripcion = panta.pedir("La descripcion no puede estar vacia! Descripcion?:")

            proveedor = panta.pedir("Ingrese el codigo del Proveedor:") #se tiene que abrir el archivo de proveedores
            while proveedor == "":                                      #y buscar por orden alfabetico
                proveedor = panta.pedir("El proveedor no puede estar vacio! Proveedor?:")


            opcion = panta.pedir("Soy Alta de Articulo")

        elif codigo == "02":
            opcion = panta.pedir("Soy baja de Articulo")
        elif codigo == "03":
            opcion = panta.pedir(f"Soy modificaciones de Articulo codigo = {codigo}")
        return

class Cliente(Persona):
    def movimientos(self, codigo):
        panta = Pantalla()
        opcion = panta.pedir("soy Cliente")
        if codigo == "01":
            opcion = panta.pedir("Soy Alta de Cliente")
        elif codigo == "02":
            opcion = panta.pedir("Soy baja de Cliente")
        elif codigo == "03":
            opcion = panta.pedir(f"Soy modificaciones de Cliente codigo = {codigo}")
        return


class Proveedor(Persona):
    def movimientos(self, codigo):
        panta = Pantalla()
        opcion = panta.pedir("Soy Proveedor")
        if codigo == "01":
            opcion = panta.pedir("Soy Alta de Proveedor")
        elif codigo == "02":
            opcion = panta.pedir("Soy baja de Proveedor")
        elif codigo == "03":
            opcion = panta.pedir(f"Soy modificaciones de Proveedor codigo = {codigo}")
        return

class Pantalla:

   def pedir(self, texto = "Ingrese Una Opcion:"):
     opcion = input(texto)
     return opcion

   def mostrar(self, listaopciones=[], titulo="Sistema de Stock"):
     print(titulo)
     for i in listaopciones:
        print(i)

   def borrarPantalla(self):  # Definimos la función estableciendo el nombre que queramos
       if os.name == "posix":
           os.system("clear")
       elif os.name == "ce" or os.name == "nt" or os.name == "dos":
           os.system("cls")


panta=Pantalla()
opcion = ""
while opcion != "04":
    listaop = ["01 - Altas", "02 - Bajas", "03 - Modificaciones", "04 - Salir"]
    panta.borrarPantalla()
    panta.mostrar(listaop)
    opcion = panta.pedir()

    while opcion not in ["01", "02", "03", "04"]:
        panta.mostrar("","Las opciones a elegir son: 01, 02 ,03 o 04 en dos caracteres!! Pruebe de nuevo!")
        opcion = panta.pedir()

    if opcion != "04":

        opcion_A = ""
        while opcion_A != "04":
            panta.borrarPantalla()
            titulo = "Menu de " + listaop[int(opcion) - 1][4:]
            listaop_A = ["01 - Cliente", "02 - Proveedor", "03 - Articulo", "04 - Menu Anterior"]
            panta.mostrar(listaop_A, titulo)
            opcion_A = panta.pedir()

            while opcion_A not in ["01", "02", "03", "04"]:
                panta.mostrar("", "Las opciones a elegir son: 01, 02 ,03 o 04 en dos caracteres!! Pruebe de nuevo!")
                opcion_A = panta.pedir()

            if opcion_A != "04":
                try:
                    file = Archivo()
                    nombre = listaop_A[int(opcion_A) - 1][5:]
                    archivo = file.abrir(f"{nombre}.txt", "a+")
                    objeto = eval(nombre)
                    obj = objeto()
                    obj.movimientos(opcion)
                except:
                    ooops = panta.pedir("Aca pasa algo!")
                    continue
                finally:
                    file.cerrar(archivo)
