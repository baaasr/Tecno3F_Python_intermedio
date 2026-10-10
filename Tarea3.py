def Programa_1():
    #Calcular el mayor de dos números ingresados por teclado usando un operador ternario
    try:
        n1=float(input("ingrese un numero: "))
        n2=float(input("Ingrese otro numero: "))

        print(f"El mayor de los 2 numeros es {n1 if n1>n2 else n2}")
    except Exception as e:
        print(f"Error: {e}")

def Programa_2(*args):

    try:
      
        entrada=input("Ingrese una serie de palabras separadas por un espacio: ")

        Buscar_palabra(*list(map(str,entrada.split())))
    except Exception as e:
        print(f"Error: {e}")
   

def Buscar_palabra(*args):
    #Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
    #print(args)
    palabra=input("Ingrese una palabra para buscar en la lista: ")
    #print(palabra)

    print(f"{"Palabra encontrada" if palabra in args else "Palabra no encontrada"}")

def Programa_3():
    #Determinar si un número es par o impar
    try:
        n1=int(float(input("Ingrese un numero par o impar: ")))

        print(f"{n1} es {"Par" if n1%2==0 else "Impar"}")

    except Exception as e:
        print(f"Error: {e}")


def Programa_4(*args):
    try:
           
        entrada=input("Ingrese una serie de numeros separados por un espacio: ")
    
        calcular_promedio(*list(map(float,entrada.split())))

    except Exception as e:
        print(f"Error: {e}")
   

def calcular_promedio(*args):
    #Calcular el promedio de una lista de números usando args y un operador ternario
    try:
        suma=0
        promedio=0
        for arg in args:
            suma+=arg
    
        promedio=suma/len(args)
    
        print(f"El promedio de todos los numeros da: {promedio}")
        print(f"La persona esta {"aprobada" if promedio>=7 else "desaprobada"}")

    except Exception as e:
        print(f"Error: {e}")

def Programa_5():
    try:
        entrada=input("Ingrese 5 valores separados por un espacio: ")
        argumentos(*list(map(str,entrada.split())))
    except Exception as e:
        print(f"Error: {e}")

def argumentos(*args):

    print(f"{"Cantidad de argumentos correctos" if len(args)>=5 else "Error: Cantidad de Argumentos insuficiente"}")
    pass

Programa_1()
#Programa_2()
#Programa_3()
#Programa_4()
#Programa_5()