"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

def convertMathImgToBipolarNumbers(img, treshold, sign=-1):
    """
        Convierte una imagen ya convertida en matriz
        a una matriz conformada por

        1 y -1
        O
        1 y signo que se quiera

        Ejemplo
        convertMathImgToBipolarNumbers([[1,1,3,2...3], [[2,1,3,2...4], ..., [4,2,2,1...2]]], 0.2)
        
        O

        convertMathImgToBipolarNumbers([[1,1,3,2...3], [[2,1,3,2...4], ..., [4,2,2,1...2]]], 0.2, 0)

        Return
        Matriz conformado por
        1 y -1

        O

        1 y (signo que se quiera)
    """
    binaryImg = (img > treshold).astype(int)
    binaryImg[binaryImg == 0] = sign

    return binaryImg