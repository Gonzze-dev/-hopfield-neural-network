"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from numpy import all

def verifyElementsOfPattern(npArray):
    """
        Verifica que los elementos del patron
        o que los elementos de un conjunto de patrones
        esten entre -1 y 1

        Ejemplo
        verifyElementsOfPattern([-1,-1,-1,1])
        O
        verifyElementsOfPattern([[-1, -1, -1, 1], [1, 1, 1, -1]])

        Return

        verifyElementsOfPattern([-1, -1, -1, 1]) -> True
        verifyElementsOfPattern([1.34, 1, 1, 1.2]) -> Exeption
    """

    value = all((npArray >= -1) & (npArray <= 1))
    
    if not value:
        raise ValueError(f"Error, todos los elementos de la matriz deben de estar entre -1 y 1")
    
    return value