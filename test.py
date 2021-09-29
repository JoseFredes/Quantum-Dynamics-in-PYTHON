import numpy as np
from getconjugated import  getTconjugated

# se crea una mM 2X2 como ejemplo
matrix = [[1+2 , 5 + 3j], [2 , 4 - 1j]]

#Se llama la a función
matrixC = getTconjugated(matrix)


#se imprime M inicial
print(matrix)

print('=============')


# Impresion de la transpuesta conjugada
print(matrixC)
