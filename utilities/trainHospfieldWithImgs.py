"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from utilities.convertImgToPattern import convertImgToPattern
from numpy import copy

def trainHospfieldWithImgs(imgPaths, hopfield):
    """
        Recibe un vector con los path de las imagenes
        
        Las convierte a patrones

        Entrena la red de hospfield

        

        Ejemplo
        trainHospfieldWithImgs(['nombreCarpeta/miImagen.png', 'nombreCarpeta/miImagen2.png'])

        Return
        
        Devuelve un objeto NnHopfield
    """
    data = []
    #convertir imagenes a patrones
    for imgPath in imgPaths:
        binaryImg = convertImgToPattern(imgPath)
        data.append(copy(binaryImg.flatten()))
    #convertir imagenes a patrones

    patterns = copy(data)
    #entrenar red
    hopfield.train(patterns)
    #entrenar red

    return hopfield