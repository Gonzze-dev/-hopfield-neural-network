"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from numpy import copy, random

def getCorrupted(pattern, corruptionLevel=0.25):
    """
        Se obtiene un patron de uno ya asociado a la matriz de pesos
        y es corrompido.
        Esta funcion es creada para poder probar que tan bien se peude
        reconstruir un patron corrompido con una red de hopfiel

        Ejemplo
        getCorrupted([-1,-1,-1,1])
        O
        getCorrupted([-1,-1,-1,1], 0.4)

        Return
        Retorna el patron corrompido
    """

    # Crear una copia de la entrada para no modificar la original
    patternCorrupted = copy(pattern)
    
    # Generar una máscara binomial para determinar qué elementos serán corrompidos
    invertion = random.binomial(n=1, p=corruptionLevel, size=len(pattern))
    
    # Aplicar la inversión a los elementos seleccionados por la máscara
    for i, v in enumerate(pattern):
        if invertion[i]:
            patternCorrupted[i] = -1 * v
    
    return patternCorrupted