"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""


from Hopfield import Hopfield
from utilities.readCsv import readCsv


def test3():
    """
    Lee un csv, entrena la red con los patrones de dicho csv
    
    Introduce un patron corrompido e intenta recomponerlo
    
    Y Imprime el resultado + el numero de iteraciones
    """
    filePath = 'csv/data.csv'
    patterns = readCsv(file=filePath)

    hp = Hopfield()

    hp.train(patterns)

    newPattern = [1,1,1,1,1,1,1,1,1,-1]
    result, iters = hp.predict(newPattern)

    print(result, iters)