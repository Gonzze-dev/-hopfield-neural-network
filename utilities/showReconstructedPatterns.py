"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from matplotlib import pyplot as plt


def showReconstructedPatterns(reconstructedList):
    """
        Muestra la matriz de cada patron en un plot

        Ejemplo
        showPatterns([[1,1,1], [1,1,1], ..., [1,1,1]])
    """
    fig, axs = plt.subplots(len(reconstructedList), #cantidad de filas segun cantidad de elementos
                            1, #una columna patron reconstruido
                            figsize=(8,8)) #tamaño de la ventana

    for i, (reconstructed) in enumerate(reconstructedList):
        axs[i].imshow(reconstructed[str(i)], cmap='viridis')
        axs[i].axis('off')
        axs[i].set_title('Reconstructed Pattern')


    plt.show()