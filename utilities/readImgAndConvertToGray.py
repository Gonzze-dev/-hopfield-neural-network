"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from skimage import io, transform, filters

def readImgAndConvertToGray(imgPath, w, h):
    """
        Convierte una imagen a gris, luego a matriz de WxH dimensiones

        Ejemplo

        readImgAndConvertToGray('nombreCarpeta/miImagen.png', 1000, 1000)
        
        w -> width -> altura

        h -> height -> anchura

        Return

        matrizImagen y threshold (umbral)
    """
    img = io.imread(imgPath, as_gray=True)
    img  = transform.resize(img, (w, h), mode='constant')
    threshold = filters.threshold_otsu(img)   

    return img, threshold