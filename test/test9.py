"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from NnHopfield import NnHopfield

from utilities.corruptMatrixImgsOfPatterns import corruptMatrixImgsOfPatterns
from utilities.reconstructPatterns import reconstructPatterns
from utilities.showPatterns import showPatterns
from utilities.trainHospfieldWithImgs import trainHospfieldWithImgs



def test9():
    """
    Entrena la red con 2 imagenes similares

    Luego las corrompe, mas una similar a las otras con la que no fue entrenada la red

    Reconstruye las imagenes corrompidas

    Muestra las imagenes en forma de patron original, corrompido, y reconstruido

    Esto se hace para ver, que tan buena es la red reconstruyendo imagenes similares
    que no conoce
    """

    imgPaths = ['imgs/cafe1.png', 
                'imgs/cafe2.png'
                ]
    imgPathsReconstruct = ['imgs/cafe1.png', 
                'imgs/cafe2.png',
                'imgs/cafe3.png'
                ]
    
    hp = trainHospfieldWithImgs(imgPaths, NnHopfield())

    mOriginal, mCorrupted, matPatterns = corruptMatrixImgsOfPatterns(imgPathsReconstruct)
    
   #falta comentar reconstructPatterns# 
    listPatterns = reconstructPatterns(matPatterns, hp)
    #sin terminar falta la muestra en plot de los patrones originales, corrompidos y reconstruidos#

    showPatterns(mOriginal, mCorrupted, listPatterns)