import numpy as np

matrix = [[1+ 2J]]


def getTconjugated(matrix):
    transp= np.transpose(matrix)
    conjugated = transp.conj()
    return conjugated


