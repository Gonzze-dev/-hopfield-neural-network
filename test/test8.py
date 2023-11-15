"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from NnHopfield import NnHopfield

from utilities.corruptMatrixImgsOfPatterns import corruptMatrixImgsOfPatterns
from utilities.reconstructPatterns import reconstructPatterns
from utilities.showPatterns import showPatterns
from utilities.trainHospfieldWithImgs import trainHospfieldWithImgs



def test8():
    """
    Entrena la red con 3 imagenes similares

    Luego las corrompe

    Reconstruye las imagenes corrompidas

    Muestra las imagenes en forma de patron original, corrompido, y reconstruido
    """
    imgPaths = ['imgs/cafe1.png', 
                'imgs/cafe2.png',
                'imgs/cafe3.png']
    
    hp = trainHospfieldWithImgs(imgPaths, NnHopfield())

    mOriginal, mCorrupted, matPatterns = corruptMatrixImgsOfPatterns(imgPaths)
    
   #falta comentar reconstructPatterns# 
    listPatterns = reconstructPatterns(matPatterns, hp)
    #sin terminar falta la muestra en plot de los patrones originales, corrompidos y reconstruidos#

    showPatterns(mOriginal, mCorrupted, listPatterns)