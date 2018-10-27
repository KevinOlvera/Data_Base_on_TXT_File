import time
import os
import re

class Cliente:
    def __init__(self, id, nombre, apellido_p, apellido_m, year, month, day, credito, deuda):
        self.Id = id
        self.Nombre = nombre
        self.ApellidoP = apellido_p
        self.ApellidoM = apellido_m
        self.YearR = year
        self.MonthR = month
        self.DayR = day
        self.Credito = credito
        self.Deuda = deuda

    def Cambiar_Fecha(self):
        self.YearR = time.strftime("%Y")
        self.MonthR = time.strftime("%m")
        self.DayR = time.strftime("%d")

    def toSave(self):
        cliente = ""
        cliente += str(self.Id) + ':'
        cliente += self.Nombre + ':'
        cliente += self.ApellidoP + ':'
        cliente += self.ApellidoM + ':'
        cliente += str(self.YearR) + ':'
        cliente += str(self.MonthR) + ':'
        cliente += str(self.DayR) + ':'
        cliente += str(self.Credito) + ':'
        cliente += str(self.Deuda)
        return cliente

def Id_Maximo():

    f = open("base.txt","r")
    lineas = f.readlines()

    id = 0

    for linea in lineas:
        aux_linea = Separar_Informacion(linea)
        id = int(aux_linea[0]) + 1
        
    f.close()

    return id

def Pedir_Datos():
    datos = []

    dato = input('Ingresa el nombre del cliente: ')
    datos.append(dato)

    dato = input('Ingresa el apellido paterno del cliente: ')
    datos.append(dato)

    dato = input('Ingresa el apellido materno del cliente: ')
    datos.append(dato)

    while True:
        dato = input('Ingresa el credito del cliente: ')
        if int(dato) >= 0:
            datos.append(dato)
            break
        else:
            print("Por favor introduce un credito mayor a 0\n")

    return datos

def Registrar_Cliente(id):
    datos = Pedir_Datos()
    cliente_registrar = Cliente(id, datos[0], datos[1], datos[2], 0, 0, 0, datos[3], 0.0)
    cliente_registrar.Cambiar_Fecha()

    f = open ('base.txt','a')
    f.write(cliente_registrar.toSave() + '\n')
    f.close()

def Separar_Informacion(cliente):
    info = cliente.split(':')
    info[8].rstrip('\n')
    return info

def Imprimir_Informacion(linea):
    cliente = Separar_Informacion(linea)
    info = ""
    info += "|  " + cliente[0] 
    info += " |  " + cliente[1] 
    info += "  |  " + cliente[2] 
    info += "  |  " + cliente[3] 
    info += "  |  " + cliente[4] + "/" + cliente[5] + "/" + cliente[6] 
    info += "  |  " + cliente[7] 
    info += "  |  " + cliente[8].rstrip('\n') + "  |"

    return info

def Buscar_Cliente_Id(valor):
    f = open ('base.txt')
    linea = f.readline()
    while linea != '':
        if re.match(valor +':', linea):
            f.close()
            return linea
        linea = f.readline()
    print("El cliente no existe D:")
    f.close()
    return False

def Buscar_Cliente_Nombre(valor):
    f = open ('base.txt')
    linea = f.readline()
    while linea != '':
        if re.match( '[0-9]+:' + valor + ':', linea):
            f.close()
            return linea
        linea = f.readline()
    print("El cliente no existe D:")
    f.close()
    return False

def Mostrar_Clientes():
    f = open ('base.txt')
    linea = f.readline()
    while linea != '':
        print(Imprimir_Informacion(linea))
        linea = f.readline()
    f.close()

def Mostrar_Cliente_Id():
    valor = input('Ingresa el ID del cliente a mostrar: ')
    cliente = Buscar_Cliente_Id(valor)

    if cliente != False:
        print("+----+----------+-----------+-----------+---------------+-----------+---------+")
        print("| ID |  Nombre  | ApellidoP | ApellidoM | Fecha de Alta |  Credito  |  Deuda  |")
        print("+----+----------+-----------+-----------+---------------+-----------+---------+")
        print(Imprimir_Informacion(cliente) + "\n")

def Mostrar_Cliente_Nombre():
    valor = input('Ingresa el Nombre del cliente a mostrar: ')
    cliente = Buscar_Cliente_Nombre(valor)

    if cliente != False:
        print("+----+----------+-----------+-----------+---------------+-----------+---------+")
        print("| ID |  Nombre  | ApellidoP | ApellidoM | Fecha de Alta |  Credito  |  Deuda  |")
        print("+----+----------+-----------+-----------+---------------+-----------+---------+")
        print(Imprimir_Informacion(cliente) + "\n")

def Eliminar_Cliente_Id():
    valor = input('Ingresa el ID del cliente a eliminar: ')
    cliente = Buscar_Cliente_Id(valor)

    f = open("base.txt","r")
    lineas = f.readlines()
    f.close()
 
    f = open("base.txt","w")

    for linea in lineas:
        if linea != cliente:
            f.write(linea)
    
    f.close()

def Modificar_Cliente():
    valor = input('Ingresa el ID del cliente a modificar: ')
    cliente = Buscar_Cliente_Id(valor)

    cliente_modificado = Editar_Cliente(Separar_Informacion(cliente))

    f = open("base.txt","r")
    lineas = f.readlines()
    f.close()
 
    f = open("base.txt","w")

    for linea in lineas:
        if linea != cliente:
            f.write(linea)
        else:
            f.write(cliente_modificado)
    
    f.close()

def Editar_Cliente(cliente):
    print(" 1.-Nombre = " + cliente[1] + "\n 2.-ApellidoP = " + cliente[2] + "\n 3.-ApellidoM = " + cliente[3] + "\n 4.-Credito = " + cliente[7] + "\n 5.-Deuda = " + cliente[8] + "\n 0.-Atras")
    menu_3 = input('¿Que quieres hacer? -> ')

    if menu_3 == '1':
        dato = input('Ingresa el nombre del cliente: ')
        cliente_modificado = Cliente(cliente[0], dato, cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[7], cliente[8])
    elif menu_3 == '2':
        dato = input('Ingresa el apellido paterno del cliente: ')
        cliente_modificado = Cliente(cliente[0], cliente[1], dato, cliente[3], cliente[4], cliente[5], cliente[6], cliente[7], cliente[8])
    elif menu_3 == '3':
        dato = input('Ingresa el apellido materno del cliente: ')
        cliente_modificado = Cliente(cliente[0], cliente[1], cliente[2], dato, cliente[4], cliente[5], cliente[6], cliente[7], cliente[8])
    elif menu_3 == '4':
        while True:
            dato = input('Ingresa el credito del cliente: ')
            if int(dato) >= 0:
                cliente_modificado = Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], dato, cliente[8])
                break
            else:
                print("Por favor introduce un credito mayor a 0\n")
    elif menu_3 == '5':
        dato = input('Ingresa la deuda del cliente: ')
        cliente_modificado = Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[7], dato)
    elif menu_3 == '0':
        pass
    else:
        print("Escoge una opcion valida.")

    return cliente_modificado.toSave()
        


if __name__ == "__main__":
  
    while(True):
        print("\nBienvenido al Sistema de Clientes de ESCOMStore :D\n 1.-Registrar un cliente\n 2.-Modificar un registro\n 3.-Borrar un registro\n 4.-Mostrar registros\n 0.-Salir")
        menu = input('¿Que quieres hacer? -> ')
        if menu == '1':
            Registrar_Cliente(Id_Maximo())
            os.system('clear')
        elif menu == '2':
            Modificar_Cliente()
        elif menu == '3':
            Eliminar_Cliente_Id()
            os.system('clear')
        elif menu == '4':
            menu_2 = input(" 1.-Mostrar por ID\n 2.-Mostrar por nombre\n 3.-Mostrar todos\n 4.-Atras\n¿Que quieres hacer? -> ")
            if menu_2 == '1':
                Mostrar_Cliente_Id()
            elif menu_2 == '2':
                Mostrar_Cliente_Nombre()
            elif menu_2 == '3':
                Mostrar_Clientes()
            elif menu_2 == '0':
                pass
            else:
                print("Escoge una opcion valida.")
        elif menu == '0':
            break
        else:
            print("Escoge una opcion valida.")