"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from matplotlib import pyplot as plt


def showPatterns(original_list, corrupted_list, reconstructed_list):
    """
        Muestra la matriz de cada patron en un plot

        Ejemplo
        showPatterns([[1,1,1], [1,1,1], ..., [1,1,1]], 
                     [[1,1,1], [1,1,1], ..., [1,1,1]],
                     [[1,1,1], [1,1,1], ..., [1,1,1]])
    """
    fig, axs = plt.subplots(len(original_list), #cantidad de filas segun cantidad de elementos
                            3, #tres columnas original corrompido y reconstruido
                            figsize=(8,8)) #tamaño de la ventana

    for i, (original, corrupted, reconstructed) in enumerate(zip(original_list, corrupted_list, reconstructed_list)):
        axs[i, 0].imshow(original, cmap='viridis')
        axs[i, 0].axis('off')
        axs[i, 0].set_title('Original Pattern')

        axs[i, 1].imshow(corrupted, cmap='viridis')
        axs[i, 1].axis('off')
        axs[i, 1].set_title('Corrupted Pattern')

        axs[i, 2].imshow(reconstructed[str(i)], cmap='viridis')
        axs[i, 2].axis('off')
        axs[i, 2].set_title('Reconstructed Pattern')

    plt.show()