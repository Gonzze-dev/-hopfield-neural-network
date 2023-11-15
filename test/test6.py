"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from NnHopfield import NnHopfield

from utilities.convertImgToPattern import convertImgToPattern
from utilities.getCorrupted import getCorrupted

from matplotlib import pyplot as plt
from numpy import copy


def test6():
    """
    Se convierte una serie de imagenes a patrones

    Se entrena la red

    Se lee una imagen con la que se entreno la red y
    se corrompe dicha imagen
   
    Se convierte a un patron
    
    Se intenta recomponer la imagen
    
    El patron de la imagen a recomponer se convierte en una matriz
    
    Se imprime las iteraciones
    
    y el patron vector que se paso a un patron matriz se muestra en un plot
    """
    imgPaths = ['imgs/cafe1.png', 
                'imgs/cafe2.png',
                'imgs/cafe3.png',
                'imgs/auto1.png']
    data = []

    #convertir imagenes a patrones
    for imgPath in imgPaths:
        binaryImg = convertImgToPattern(imgPath)
        data.append(copy(binaryImg.flatten()))
    #convertir imagenes a patrones

    patterns = copy(data)
    #entrenar red
    hp = NnHopfield()
    hp.train(patterns)
    #entrenar red

    imgPath = 'imgs/cafe3.png'

    #convertir imagen a patrones
    binaryImg = convertImgToPattern(imgPath)
    newPattern = copy(binaryImg.flatten())
    newPatternCorrupted = getCorrupted(newPattern)
    
    #convertir imagen a patrones

    result, iters = hp.predict(newPatternCorrupted, maxIterations=100)
    
    #convertir vector del patron a matriz
    mathImg = result.reshape((100,100))
    #convertir vector del patron a matriz
    print(iters)

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(mathImg, cmap='gray')
    plt.title('Imagen Original')
    plt.show()