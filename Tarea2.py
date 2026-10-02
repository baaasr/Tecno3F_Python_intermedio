#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

def Dividir(a,b):
    return a/b

def Programa_1():
    try:
        a=float(input("Ingrese un numero como dividendo: "))
        b=float(input("Ingrese otro numero como divisor: "))

        print(f"{a}/{b} es igual a {Dividir(a,b)}")
    except ZeroDivisionError:
        print(f"Error: No se puede dividir por cero")
    except Exception as e:
        print(f"Error: {e}")

#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario

def Programa_5():
    try:
        a=float(input("Ingrese un numero como dividendo: "))
        b=float(input("Ingrese otro numero como divisor: "))

        print(f"{a}/{b} es igual a {Dividir(a,b)}")

    except ValueError:
        print(f"Error: Numero no valido")
    except ZeroDivisionError:
        print(f"Error: No se puede dividir por cero")
    except Exception as e:
        print(f"Error: {e}")

#Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario

def Sumar(a,b="Hola"):
    return a+b

def Programa_2():
    try:
        a=float(input("Ingrese un numero: "))
        #b=float(input("Ingrese otro numero para sumarle: "))

        print(f"La sumatoria es igual a {Sumar(a)}")
        #print(f"Un 1 + Hola ={1+"Hola"}")
    except TypeError:
        print(f"Error: Solo se pueden sumar numeros")
    except Exception as e:
        print(f"Error: {e}")

#Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

def Programa_3():
    try:

        dict={
            "Nombre":"Antonella",
            "Apellido":"Lasorsa"
        }
        print(dict)

        clave=input("Ingrese una clave del diccionario: ")

        print(f"Su {clave} es {dict[clave]}")
    except KeyError:
        print(f"Error: Clave inexistente")
    except Exception as e:
        print(f"Error: {e}")

# Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.

def Programa_4():
    try: 
        list=[]
        with open("n_arch.txt", "r") as archivo:
            list=archivo.readlines()

        print(list)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado")

        with open("n_arch.txt", "w") as archivo:
            archivo.write("Hola mundo")
    except Exception as e:
            print(f"Error: {e}")


Programa_1()
#Programa_2()
#Programa_3()
#Programa_4()
#Programa_5()