# import random

# player = int(input("Introduce un numero del 1 al 10: -- "))
# num = random.randrange(1,10)
# intentos = 0
# while player != num:
#     intentos += 1
#     num = random.randrange(1,10)
#     player = int(input("has fallado, introduce un numero del 1 al 10 nuevamente: -- "))        
# else:
#     print("Has acertado, tus intentos fueron: " + str(intentos))
#################################
# comprobacion = 2+4+6+8+10+12+14+16+18+20
# print(comprobacion)
# n = 2
# suma = 0
# while n <= 20:
#     if n % 2 == 0:
#         suma += n
#     n += 1
# print(suma)
##################################
# comp = 120+123+126+129+132
# print(comp)
# num1 = int(input("Introduce un numero"))
# num2 = int(input("Introduce another number"))
# suma = 0
# while num1 <= num2:
#     if num1 % 3 == 0:
#         suma += num1
#     num1 += 1
# print(suma)
##################################
# contraseña = "NehuenGarcia123123"
# usuario = "najc8d"
# ingresoContraseña = input("Ingrese contraseña: ")
# ingresoUser = input("Ingrese el usuario: ")
# attemps = 0
# while contraseña != ingresoContraseña or usuario != ingresoUser:
#     if ingresoUser != usuario:
#         ingresoUser = input("Usuario Incorrecto, ingrese nuevamente: ")
#     if ingresoContraseña != contraseña:
#         ingresoContraseña = input("Contraseña Incorrecta, ingrese nuevamente: ")
#     attemps += 1
#     if attemps >= 10:
#         print("has alcanzado el maximo de intentos, ingrese email para la recuperacion de la contraseña")
#         email = input("email: ")
#         break
# else:
#     if contraseña == ingresoContraseña: print("Contraseña correcta")
##################################
# numero = int(input("Ingrese un numero del 1 al 5: "))
# vocal = input("Ingrese una vocal")
# number = 3
# vowel = "a"
# puntos = 100
# while numero != number or vocal != vowel:  
# #
#     if (numero == number) or (vocal == vowel):
#         puntos -= 2
#     else:
#         puntos -= 5
#     numero = int(input("Ingrese un numero del 1 al 5: "))
#     vocal = input("Ingrese una vocal")
# else:
#     print("Son equals right now")
# print(puntos)
##################################
# a = "altura"
# b = "parte"
# c = "cristal"

# d = b[:4] + c[2:3] + a[2:]
# print(d)
##################################
# n = 0
# cadena = input("Introduce una cadena de caracteres")
# longitud = len(cadena)
# if longitud < 20:
#     while n < longitud:
#         print(cadena[n])
#         n += 1
# else:
#     print("La cadena no puede ser superior a 20 caracters")
##################################
# cadena = """ Muchos años después, frente al pelotón de
# fusilamiento, el coronel Aureliano Buendía había de
# recordar aquella tarde remota en que su padre lo llevó
# a conocer el hielo. """
# long = len(cadena)
# n = 0
# veces = 0
# while n < long:
#     if cadena[n] == "o" or cadena[n] == "O" or cadena[n] == "ó" or cadena[n] == "Ó":
#         veces += 1
#     n += 1
# print(veces)
##################################
# cadena = input("Ingrese la palabra: ")
# vowels = "aeiouáéíóú"
# consonantes = "zxcvbnmsdfghjklñpqwrty"
# i = 0
# contador = 0
# contadorConsonantes = 0
# while i <= len(cadena)-1:
#     if cadena[i] in vowels:
#         contador += 1
#     elif cadena[i] in consonantes:
#         contadorConsonantes += 1
#     i += 1
# print(contador)
#################################
# mamiferos = ("tigre","gato","leon")
# aves = ("aguila","buitre","canario")
# reptiles = ("tortuga","serpiente")
# mascotas = aves[2:3] + mamiferos[1:2] + reptiles[0:1]
# print(mascotas)
#################################
# i = 0
# lista = []
# while len(lista) <= 100:
#     lista += [i]
#     i += 1
# print(lista)
#################################
# a = range(1,16,3)
# print(5 in a)
#################################
# num = int(input("Introduce un numero entre el 18 al 25: "))
# while num in range(18,26):
#     num = int(input("Introduce otro num entre el 18 al 25: "))
#################################
# probando = True

# while probando:
#     num = int(input("introduce un numero entre el 18 al 25: "))
#     if num in range(18,26):
#         print("we are in range")
#     else:
#         print("malcihimo")
#         probando = False
#################################
# colores = ["rojo","azul","negro","amarillo","anaranjado"]
# probando = True
# colorPersons = ""
# puntos = 0
# while probando:
#     colorPersons = input("Introduce un color: ")
#     if colorPersons in colores:
#         print(colorPersons)
#         puntos += 1
#         print("Has acertado, tienes:", puntos,"puntos") 
#     else:
#         print("Malichimo")
#         probando = False
#################################
# total = 0
# for i in range(5):
#     numingre = int(input("introduce numero"))
#     total += numingre
# print(total)
#################################
# activo = True
# total = 0
# while activo:
#     if total >= 100:
#         print(total)
#         break
#     else:
#         n = int(input("Introduce un numero"))
#         total += n
#################################
# letras = ["f","g","h","l","m","p","s"]
#################################
# for i in letras:
#     print(i)
# ll d= False
# num = int(input("Ingrese un numero: "))
# lista = [28,36,43,52,61,75,84,97]
# for i in lista:
#     if (num + i) >= 100:
#         ll = True
# if ll == True:
#     print("El numero cumple la condicion:", num,"")
# else:
#     print("El numero no cumple la condicion")
#################################
# lista = [28,36,43,52,61,75,84,97]
# num = int(input("Introduce un numero: "))
# if 100 - num in lista:
#     print("El numero cumple la condicion")
# else:
#     print("El numero no cumple la condicion")    
#################################
# lista = [28,36,43,52,61,75,84,97]
# num = int(input("Dime un numero: "))
# encontrado = False

# for elemento in lista:
#     if num + elemento == 100:
#         encontrado = True

# if encontrado == True:
#     print("El numero cumple la condicion ")
# else:
#     print("El numero no cumple la condicion ")
#################################
# lista = [28,36,43,52,61,43,75,84,43,97,36,36,36,36]
# numero = 36
# contador = 0
# for i in lista:
#     if numero == i:
#         contador += 1
# print(contador)
# #################################
# meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
# meses_con_b = ()
# for mes in meses:
#     if "b" in mes:
#         meses_con_b += (mes,)
# print(meses_con_b)
# lista = [2,5,90,23,45,87,54,11,38]
# elementon = 2
# for elemento in range(len(lista)):
    # if elementon == lista[elemento]:
        # print("el indice se encuentra en",elemento)
#################################
# num = int(input("Ingrese un numero"))

# for i in range(10):
#     print(str(num),"*", str(i+1)," =", str((i+1)*num))
#################################

# numero = 9000
# secuencia = range(1,492023)

# for i in secuencia:
#     if i == numero:
#         print("Tenemos el número.", i)
#         break
#     else:
#         print("we don't have anithyng")
#################################
# temperatura = [19,22,21,24,23,27,21,20,19,18,21,20]
# rango = range(18,25)
# for i in temperatura:
#     if i in rango:
#         print("Temperatura adecuada.", i)
#     else:
#         print("Temperatura incorrecta.", i)
#         print("Encendiendo Ventiladores...")
#         break
#################################
# letra = "d"
# while True:
#     letraUser = input("Introduce una letra")
#     if letraUser == "w":
#         print("La letra w no esta permitida")
#         break
#     elif letraUser == letra:
#         print("Letra correcta.")
#         break
#     else:
#         print("Letra incorrecta, seguí intentando.")
#################################
# letra = "h"
# palabra = "zanahoria"
# for i in palabra:
#     if i != letra:
#         print(i)
#         if i == letra:
#             continue
#################################
# numeros = [1,4,-3,5,0,7,-2,6,0,0,2,3,0,0,2,3]
# for i in numeros:
#     if i == 0:
#         continue
#     if i > 0:
#         print("Es mayor", i)
#     else:
#         print("Es menor", i)   
#################################
# import math
# print(math.sqrt(9))
# def perimetro():
#     r = int(input("Ingrese ratio"))
#     cal = 2 * math.pi * r
#     return cal
# print(perimetro())
# print(dir(math))
#################################
# from math import pi, sqrt

# def Ar():
#     r = int(input("Ingrese radio"))
#     area = pi * (r ** 2)
#     return area
# print(Ar())
#################################
# from math import sqrt

# def pitagoras(a, b):
#     c = sqrt((a ** 2) + (b ** 2))
#     return c

# print(pitagoras(3,4))
#################################
# from math import pi, sqrt

# def perimetro(r,s):
#     p = 2 * pi * sqrt((s**2+r**2)/2)
#     return p


# r = int(input("Ingrese el lado R"))
# s = int(input("Ingrese el lado S"))

# print(perimetro(r,s))
#################################
# import random
# print(dir(random))
# def jogo(nume):
#     intentos = 0
#     while True:
#         if intentos < 6:
#             intentos += 1
#             numP = int(input("Ingrese un numero "))
#             if numP == nume:
#                 print("Has ganado, has adivinado el numero ")
#                 break
#             if numP > nume:
#                 print(random.choice(['demasiado alto','uff te has pasado', 'pero que haces chaval']))
#             else:
#                 print(random.choice(['demasiado bajo','uf muy bajo','pero estas cavando un pozo chaval']))
#         else:
#             print("Has superado los intentos permitidos")
#             break
#     return numP
# nume = random.randint(1,100)
# print(jogo(nume))
#################################
# from random import randint
# def tiradamoneda(a,b):
#     for l in range(100):
#         l = (randint(1,2))
#         if l == 1:  
#             a += 1
#         else:
#             b += 1
#     return print("Cara salieron", a, " y seca: ", b)
# contadorCara = 0
# contadorSeca = 0
# tiradamoneda(contadorCara,contadorSeca)
#################################
# from random import choice, randint
# jugando = True
# while jugando:
#     a = choice(["Papel","Tijeras","Piedras"])
#     b = input("Elige: Papel, Piedra o Tijeras:    ")
#     print("...Comenzando...")
#     print("La maquina saco", a)
#     ganador = ""
#     if a == b:
#         print("Empate")
#     elif a == "Papel" and b == "Tijeras":
#         print = "El que gano fue: --Jugador 2--"
#     elif a == "Papel" and b == "Piedra":
#         print = "El que gano fue: --Jugador 1--"
#     elif a == "Tijeras" and b == "Piedra":
#         print = "El que gano fue: --Jugador 2--"
#     elif a == "Tijeras" and b == "Papel":
#         print = "El que gano fue: --Jugador 1--"
#     elif a == "Piedra" and b == "Papel":
#         print = "El que gano fue: --Jugador 2--"
#     elif a == "Piedra" and b == "Tijeras":
#         print = "El que gano fue: --Jugador 1--"
#     elif b == "Papel" and a == "Tijeras":
#         print = "El que gano fue: --Jugador 1--"
#     elif b == "Papel" and a == "Piedra":
#         print = "El que gano fue: --Jugador 2--"
#     elif b == "Tijeras" and a == "Piedra":
#         print = "El que gano fue: --Jugador 1--"
#     elif b == "Tijeras" and a == "Papel":
#         print = "El que gano fue: --Jugador 2--"
#     elif b == "Piedra" and a == "Papel":
#         print = "El que gano fue: --Jugador 1--"
#     elif b == "Piedra" and a == "Tijeras":
#         print = "El que gano fue: --Jugador 2--"    
#     print("Jugamos otra partida")
#     seguir = input("Quiere volver a jugar (s/n) ")
#     if seguir == "n":
#         jugando = False
#######################
# import time

# inicio = time.time()

# while True:
    
#     print("Estamos jugando ...")
    
#     final = time.time()
    
#     if final - inicio >= 5:
#         break
# print("Fin del juego")
# print("tiempo de juego:", final - inicio)
#######################
# import time
# import random

# print("******** CONCURSO MATEMÁTICO ********")
# print("")
# print("Haz todas las operaciones que puedas. Tienes 10 segundos de tiempo.")
# print("")
# print("*************************************")
# input("Pulse enter para iniciar: ")

# inicio = time.time()
# Tiempo = True
# puntos = 0
# while Tiempo:
#     final = time.time()
#     if final - inicio >= 10:
#         break
#     var1 = random.randint(1,10)
#     var2 = random.randint(1,10)
#     ope = random.choice(["+","-","/","*"])
#     print(time.time()/365/24/60/60)
#     if ope == "+":
#         respuesta = int(input("La cuenta es" + " " + str(var1) + " + " + str(var2) + ":"))
#         if respuesta == var1 + var2:
#             puntos += 1
#             print("Correcto, tienes", puntos, "puntos...")
#         else:
#             print("Incorrecto, tienes", puntos, "puntos")
#     elif ope == "-":
#         respuesta = int(input("La cuenta es" + " " + str(var1) + " - " + str(var2) + ":"))
#         if respuesta == var1 - var2:
#             puntos += 1
#             print("Correcto, tienes", puntos, "puntos...")
#         else:
#             print("Incorrecto, tienes", puntos, "puntos")
#     elif ope == "/":
#         respuesta = int(input("La cuenta es" + " " + str(var1) + " / " + str(var2) + ":"))
#         if respuesta == var1 / var2:
#             puntos += 1
#             print("Correcto, tienes", puntos, "puntos...")
#         else:
#             print("Incorrecto, tienes", puntos, "puntos")
#     else:
#         respuesta = int(input("La cuenta es" + " " + str(var1) + " * " + str(var2) + ":"))
#         if respuesta == var1 * var2:
#             puntos += 1
#             print("Correcto, tienes", puntos, "puntos...")
#         else:
#             print("Incorrecto, tienes", puntos, "puntos")
##############################################
# import time


# print("Comienzo del programa.")


# inicio = time.time()

# time.sleep(.5)

# final = time.time()

# print("Tiempo del programa.", final-inicio)
##############################################
# from calendar import c
# import time

# input("Presione 'Enter' para comenzar")
# tiempoI = time.time()
# c = True
# tiempoF = time.time()
# s = 10
# for s in range(10,0,-0.5):
#     if tiempoF - tiempoI >= 10:
#         break
#     print(s)
#     time.sleep(.5)
#     tiempoF = time.time() 
##############################################
# import time

# inicio = time.time()

# for i in range(21):
#     print((20-i)/2)
#     time.sleep(.5)
    
# final = time.time()

# print("Tiempo:", final - inicio - 0.5)
##############################################

# import time

# ini = time.perf_counter()
# # for i in range (1,1000000,1):
# #     print(i)
# cont = 0
# while cont != 1000000:
#     cont += 1
#     print(cont)
# fini = time.perf_counter()
# print("El tiempo de ejercucion de este for fue de: ", fini-ini)
##############################################
# import time
# from tkinter import N
# inicio = time.perf_counter()

# suma = 0

# for i in range(1, 1_100_001):
#     suma += i
# final = time.perf_counter()

# print("La suma es:", suma, "El tiempo de ejecucion para el bucle 'for' fue", final-inicio)

# inicio = time.perf_counter()

# suma = 0
# n = 1

# while n < 1_000_001:
#     suma += n
#     n += 1
    
# final = time.perf_counter()
# print("La suma es:", suma, "El tiempo de ejecucion para el bucle 'While' fue", final-inicio)
##############################################
# from random import sample, shuffle
# import time

# colores = ['rojo','azul','verde','amarillo','negro','blanco','beige','cafe','chocolate','violeta']
# puntos = 0
# while True:
#     print("MEMORIZA LOS COLORES... EL JUEGO")
#     print("... Preparado ...")
#     sampleados=sample(colores, 4)
#     print(sampleados)
#     time.sleep(3)
#     t = 0
#     for k in range(15):
#         t += 1
#         for i in range(t):
#             print("#")
#     primero = input("Primero: ")
#     segundo = input("Segundo: ")
#     tercero = input("Tercero: ")
#     cuarto = input("Cuarto: ")
#     if sampleados[0] == primero and sampleados[1] == segundo and sampleados[2] == tercero and sampleados[3] == cuarto:
#         puntos += 1
#         print("has acertado tienes: ", puntos)
#     else:
#         print("Te has equivocado")
#         continuar = input("Quieres continuar?.. s/n")
#         if continuar == "n" or continuar =="N":
#             break
#         else:
#             print("Perfecto, comencemos nuevamente")
##############################################

# cadena = "Artefacto"

# cadenaMayus = cadena.upper()

# print(cadenaMayus)

# otraCadena = "ARTILUGIO"

# otraCadenaMin = otraCadena.lower()

# nombre = nombre.capitalize() 

# nombre = nombre.title()

# print(otraCadenaMin)

# nombre = input("Hola, ¿Quién eres? ")

# nombreMayus = nombre.upper()
#print("Hola", nombre.title())
# respuesta = input("¿Seguro que eres "+nombreMayus+"?")
# if respuesta.lower() == "s":
#     print("Vale")
# else:
#     print("NonVale")
##############################################

# cadena = """Estaba allí. Era un pájaro en la ventana. Pero entonces,
# de repente, se echó a volar."""

# cadenasplit = cadena.split()

# for i in cadenasplit:
#     pala = i.strip(".")
#     print(pala.strip(","))
    
# for p in cadenasplit:
#     if "," in p:
#         n = p.strip(",")
#     elif "." in p:
#         n = p.strip(".")
#     else:
#         n = p
#     print(n)
##############################################

# cadena = "Hola {} {}.".format("Jose","Garcia")
# print(cadena)

# saludo = "Hola {} {}." "Encantando de conocerle."
# print(saludo.format("Jose","Fernandez"))
# while True:
    # l = input("Quien envia la carta? ")
    # print("MODELO DE CARTA")
    # print("Introduzca los datos de la persona:")
    # t = input("Tratamiento (Sr/Sra) : ")
    # n = input("Nombre: ")
    # a = input("Apellido: ")
    # print("")
    # print("")
    # # Mensaje = "{}. {} {}:"
    # # MensajeForm = (Mensaje.format(t,n,a))
    # # print(MensajeForm.title())
    # # print("Le escribo para informe")
    # # print("de que ha sido usted invitado")
    # # print("a la fiesta de la Empresa")
    # # print("Atentamente")
    # #############
    # print("{}. {} {}:".format(t.title(),n.title(),a.title()))
    # print("Le escribo para informarle")
    # if t.lower() == "sr":
    #     print("de que ha sido usted invitado")
    # elif t.lower() == "sra":
    #     print("de que ha sido usted invitada")
    # print("a la fiesta de la Empresa.")
    # print("Atentamente. {}.".format(l.title()))
    # print()   
    # respuesta = input("Desea imprimir otra carta (s/n): ")
    # if respuesta.lower() == "n":
    #     break
##############################################
# print()
# print("PRESUPUESTO".center(50))
# print()

# compras = [["Tornillos",723,23.2],
#            ["Tuercas",324,4.5],
#            ["Arandelas",25,35],
#            ["Puntas",1431,2.15]]

# for c in compras:
#     print("{0:12}: {1:8d} * {2:8.2f} = {3:12.2f}".format(c[0], c[1], c[2], c[1]*c[2]))
##############################################
# n = [1,2,3,4] 

# print(id(n))

# n += [5]
# # print(id(n))
# numeros = [1,2,3,4,5]

# numeros.append(6)

# numeros.append([9,10])
# print(numeros)


# lista=[]

# for n in range(100):
#     lista.append(n+1)
# print(lista)

# lista = []

# for n in range(100):
#     lista += [n+1]
# print("..",lista)

# listaPar = []
# listaImpar = []
# numeros = [2,3,5,8,9,12,21,24,25,28]
# for n in numeros:
#     if n % 2 == 0:
#         listaPar.append(n)
#     else:
#         listaImpar.append(n)
# print("Los numeros pares son", listaPar)
# print("Y los numeros impares son",listaImpar)
##############################################
# productos = []
# while True:
#     producto = input("Dime un producto ('s' para salir) : ")
#     if producto.lower() == "s":
#         print("Compras terminadas")
#         break
#     productos.append(producto)
# print("La lista de productos es: ")
# for i in productos:
#     print(i)
##############################################
# lista_compra = ["pan","leche","fruta"]

# mas_compra = ["sal","azucar"]

# lista_compra.extend(mas_compra)

# print(lista_compra)

# n = [1,2,3]
# m = [4,5]

# n.extend(m)

# print(n)

# t = [1,2,3,4]
# j = [5]

# t.extend(j)
# print(t)
##############################################
# n = [1,2,3,5]
# m = 4
# n.insert(3,m)
# print(n)

m = 1
n = [2,3]
s = [4]
t = 5

lista = []
lista.append(m)
lista.extend(n)
lista.insert(3,s[0])
lista.append(t)
print(lista)