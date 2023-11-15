"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from NnHopfield import NnHopfield
from utilities.readCsv import readCsv

from numpy import array

def test5():
    """
    Lee un csv, entrena la red con los patrones de dicho csv
    
    Introduce un patron corrompido con un numero
    de neuronas mas grande que el que ya se tiene
    e intenta recomponerlo

    se produce un error de tipo ValueError
    """
    try:
        filePath = 'csv/data.csv'
        data = readCsv(file=filePath)
        patterns = array(data)

        hp = NnHopfield()

        hp.train(patterns)

        #Patron mayor al numero de neuronas
        newPattern = [1,1,1,1,1,1,1,1,1,-1,1]
        result, iters = hp.predict(newPattern)

        print(result, iters)
    except Exception as e:
        print(e)

    print('sigue')