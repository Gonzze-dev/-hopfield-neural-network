"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from utilities.convertImgToPattern import convertImgToPattern
from utilities.readCsv import readCsv

from numpy import copy

def getPatterns(arrPathCsv=[], arrImgs=[]):
    """
        Busca y lee los archivos csv

        Busca las imagenes y las convierte a patrones

        Los agrega a una lista en comun para luego procesar los patrones
        
        Ejemplo:
        getPatterns(arrPathCsv=['nombreCarpeta/miCsv1.csv', 'nombreCarpeta/miCsv2.csv'])

        O

        getPatterns(arrImgs=['nombreCarpeta/miImagen1.png', 'nombreCarpeta/miImagen2.jpg'])
        
        O

        getPatterns(arrPathCsv=['nombreCarpeta/miCsv1.csv', 'nombreCarpeta/miCsv2.csv'], arrImgs=['nombreCarpeta/miImagen1.png', 'nombreCarpeta/miImagen2.jpg'])
    """

    data = []

    if (len(arrPathCsv) + len(arrImgs)) == 0:
        raise Exception('error, debe de ingresar algun csv o alguna imagen para entrenar la red')

    if len(arrPathCsv) > 0:
        for filePath in arrPathCsv:
            dataCsvArr = readCsv(file=filePath)

        for pattern in dataCsvArr:
            data.append(copy(pattern))

    if len(arrImgs) > 0:

        for imgPath in arrImgs:
            binaryImg = convertImgToPattern(imgPath)
            data.append(copy(binaryImg.flatten()))

    return data