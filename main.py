

"""
Antes de ejecutar el programa, hay que instalar la librería sympy ejecutando el 
siguiente comando en la consola o cmd:

pip install sympy

Hay que tener instalado pip, o descargar python desde la microsoft store

Para obtener la versión de python de la microsoft store, 
se puede ejecutar en la terminal el siguiente comando en el cmd:

python

Recomiendo correr el programa en la cmd ya que ahí sí se limpia la pantalla, 
en la terminal integrada de visual code, esto no sucede.

"""

import os
from sympy import * 
from metodos import *

x=symbols('x') #Inicializar la variable x


def menu():

    faux = (10/((x+1)**2)) #Función por defecto
    a=0 #limite inferior
    b=0 #limite superior
    n=0 #Numero de particiones

    f = Func(faux)

    select = 0

    while select != 2:
        os.system('cls')
        print("\nAproximación de integrales definidas\n\n")
        print(f"Función actual: {faux}")
        print("1. Método del trapecio")
        print("2. Salir")

        try: #try except para validar el input
            select = int(input("\nIntroduzca la opción a realizar: "))
            if (select <= 0 or select >= 7):
                print("Opción inválida")
                os.system("pause")
        except Exception as err:
            if (err == KeyboardInterrupt): raise KeyboardInterrupt #Permite usar ctrl+c para terminar en seco el programa
            print("Opción inválida")
            os.system("pause")
            select = 0


        while (select == 1): #Método del trapecio
            os.system("cls")
            try:
                print("\nSolo se consideran intervalos válidos los encontrados dentro de [0, +inf)")
                a = float(input("\nIngrese el límite inferior: "))
                b = float(input("Ingrese el límite superior: "))
                n = int(input("Ingrese el número de particiones: "))
                if (a < 0 or b < 0 or b-a <=0 or n<=0): raise Exception("Los valores dados no son validos")
                metodo_trapecio(a,b,n,f)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 1 #Si se introduce y, se vuelve al menú
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                select = 0
                os.system("pause")


class Func():
    def __init__(self,f): #Inicializar función ingresada (en este caso la por defecto)
        self.f= f

    def eval_function(self,input):
        return self.f.subs(x,input) #Evaluar un punto en la función

    def __str__(self):
        return str(self.f)

menu() #Ejecuta el programa


