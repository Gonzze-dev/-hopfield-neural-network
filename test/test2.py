"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from Hopfield import Hopfield

def test2():
    """
        
    Introduce 2 patrones, entrena la red, 
        
    Introduce un patron corrompido e intenta recomponerlo
        
    y imprime el resultado
    """
    hp = Hopfield()

    patterns = [[1,1,1,-1], [-1,-1,-1,1]]
    
    hp.train(patterns)

    newPattern = [-1,-1,-1,-1]
    result = hp.predict(newPattern)

    print(result)