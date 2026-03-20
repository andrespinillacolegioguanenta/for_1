# Programa para calcular los multiplos de 7 y 9 que hay entre el 1000 y el 5000

# -----------------
# libraries
# -----------------
print("--------------------------------------------")
print("--------calculo pares e impares----------")
print("--------------------------------------------")
import math


# -----------------
# input
# -----------------
multiplos_de_7 = 0
multiplos_de_9 = 0


# -----------------
# processing
# -----------------
for i in range(1000, 5001):

    if i % 7 == 0:
        multiplos_de_7 += 1
    else:
        pass

    if i % 9 == 0:
        multiplos_de_9 += 1
    else:
        pass



# -----------------
# output
# -----------------
print("--------------------------------------------")
print("La cantidad de múltiplos de 7 son:", multiplos_de_7)
print("--------------------------------------------")
print("La cantidad de múltiplos de 9 son:", multiplos_de_9)
print("--------------------------------------------")




