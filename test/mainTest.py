"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from NnHopfield import NnHopfield
from utilities.getPatterns import getPatterns
from utilities.reconstructPatterns import reconstructPatterns
from utilities.showReconstructedPatterns import showReconstructedPatterns

def mainTest():
    """
        Test previo a crear el main
    """
    csvPaths = ['csv/data.csv']

    imgPaths = ['imgs/cafe1.png', 
                    'imgs/cafe2.png',
                    'imgs/cafe3.png']

    hopfield = NnHopfield()

    data = getPatterns(csvPaths, imgPaths)

    hopfield.train(data)

    dataImgTest = getPatterns(arrImgs=imgPaths)

    listPatterns = reconstructPatterns(dataImgTest, hopfield)

    showReconstructedPatterns(listPatterns)