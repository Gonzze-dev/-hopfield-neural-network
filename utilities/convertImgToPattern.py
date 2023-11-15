"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from utilities.readImgAndConvertToGray import readImgAndConvertToGray
from utilities.convertMathImgToBipolarNumbers import convertMathImgToBipolarNumbers


def convertImgToPattern(imgPath, w=100,h=100, sign=-1):
    """
        Convierte una imagen a una matriz conformada por 1 y (signo que se quiera)

        Ejemplo
        convertImgToPattern('nombreCarpeta/miImagen.png')

        O

        convertImgToPattern('nombreCarpeta/miImagen.png', 1000)

        O

        convertImgToPattern('nombreCarpeta/miImagen.png', 1000, 1000)

        O

        convertImgToPattern('nombreCarpeta/miImagen.png', 1000, 1000, 0)

        
        w -> width -> altura

        h -> height -> anchura

        Return
        Matriz conformado por
        1 y -1

        O

        1 y (signo que se quiera)

        Dependiendo de si se quiere trabajar de forma binaria o bipolar
    """
    img, treshold = readImgAndConvertToGray(imgPath, w, h)
    binaryImg = convertMathImgToBipolarNumbers(img, treshold, sign)

    return binaryImg
    