"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from utilities.convertImgToPattern import convertImgToPattern
from utilities.getCorrupted import getCorrupted

from numpy import copy


def corruptMatrixImgsOfPatterns(imgPaths, w=100, h=100):
    """
        Convierte un conjunto de imagenes a patrones y las corrompe

        Ejemplo
        trainHospfieldWithImgs(['nombreCarpeta/miImagen.png', 'nombreCarpeta/miImagen2.png'])

        O

        trainHospfieldWithImgs(['nombreCarpeta/miImagen.png', 'nombreCarpeta/miImagen2.png'], 1000)

        O
        trainHospfieldWithImgs(['nombreCarpeta/miImagen.png', 'nombreCarpeta/miImagen2.png'], 1000, 1000)

        Return
        
        Devuelve una matriz con los patrones corrompidos ya convertido a matrizes
        la matriz original con los patrones sin corromper
        y la matriz con los patrones no convertido a matrizes
    """

    dataOriginal = []
    dataCorrupted = []
    matPattern = []
    umbralCorruption = 0.4
    
    #convertir imagen a patrones
    for imgPath in imgPaths:
        binaryImg = convertImgToPattern(imgPath)
        matPattern.append(copy(binaryImg.flatten()))

        dataOriginal.append(copy(binaryImg))
        
        patternCorrupted = getCorrupted(binaryImg, umbralCorruption)
        dataCorrupted.append(copy(patternCorrupted))

        
    return dataOriginal, dataCorrupted, matPattern
    
