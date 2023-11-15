"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from Hopfield import Hopfield

def test1():
    """
        Introduce 2 patrones, entrena la red, 
        
        y imprime la matriz de pesos
    """
    hp = Hopfield()

    patterns = [[1,1,1,-1], [-1,-1,-1,1]]
    weight = hp.train(patterns)

    print(weight)