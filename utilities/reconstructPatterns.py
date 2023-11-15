"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from numpy import copy

def reconstructPattern(pattern, hopfield, maxIterations=100):
    """
        Reconstruye un paatron con hopfield

        Ejemplo

        reconstructPattern([1,1,1,-1], objetoHopfield)
        
        O

        reconstructPattern([1,1,1,-1], objetoHopfield, 10)

        Return

        Retorna un patron en forma de matriz para ser reconstruido
    """
    newPattern = copy(pattern)

    result, iters = hopfield.predict(newPattern, maxIterations=maxIterations)
    
    math = result.reshape((100,100))

    return math, iters


def reconstructPatterns(patterns, hopfield, maxIterations=100):
    """
        Reconstruye un conjunto de paatrones con hopfield

        Ejemplo

        reconstructPattern([[1,1,1,-1], [1,1,1,-1], ... [1,1,1,-1]], objetoHopfield)

        O
        
        reconstructPattern([[1,1,1,-1], [1,1,1,-1], ... [1,1,1,-1]], objetoHopfield, 10)

        Return

        Retorna una lista de patrones en forma de una lista de diccionarios
        de la siguiente forma

        [{'1': [[1,1,1,-1], [-1,1,-1,-1], ... [1,1,1,-1]], 'iters': 3},

        {'2': [[1,1,1,-1], [1,-1,-1,-1], ... [1,1,1,-1]], 'iters': 2},

        ...

        {'n': [[1,1,1,-1], [-1,-1,-1,-1], ... [1,1,1,-1]], 'iters': n}]
    """

    i = 0
    listPatterns = []

    for pattern in patterns:
        newPattern, iters = reconstructPattern(pattern, hopfield, maxIterations=maxIterations)
        listPatterns.append({str(i): newPattern, 'iters': iters})
        i += 1

    return listPatterns
        