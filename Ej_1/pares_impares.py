# Programa para calcular el gasto de agua de una vivienda

# -----------------
# libraries
# -----------------

print("--------------------------------------------")
print("--------calculo del gasto del agua----------")
print("--------------------------------------------")
import math

# -----------------
# input
# -----------------

CANT_PARES = 0
CANT_IMPARES = 0
LISTA_NUMEROS ="NUEMEROS: "

# -----------------
# processing
# -----------------

for i in range (1, 6):
    n=int(input("Digite el numero " + str(i)+":"))
    LISTA_NUMEROS = LISTA_NUMEROS + str(n) +" "
    m = n%2
    if(m==0):
        CANT_PARES = CANT_PARES+1
    else:
        CANT_IMPARES = CANT_IMPARES+1



# -----------------
# output
# -----------------

print("--------------------------------------------")
print("------------------Resultado-----------------")
print("--------------------------------------------")
print("La cantidad de pares son: " + str(CANT_PARES))
print("--------------------------------------------")
print("La cantidad de impares son: " + str(CANT_IMPARES))
print("--------------------------------------------")
print(LISTA_NUMEROS)