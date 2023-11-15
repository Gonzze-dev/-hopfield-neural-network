"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from numpy import copy

def convertToVectorBipolar(*args):
        """
            Funcion de signo. 
            Si el elemento es mayor igual a 1, el elemento cambia a 1
            Si el elemento es emnor a 1, cambia a -1

            Ejemplo
            convertToVectorBipolar([3,2,4,2])

            Return
            Retorna un vector con signos 1 y -1
        """
        resultPattern = args[0][0]

        #Copia los elementos de la matriz, para no mutar elementos por referencia
        aux = copy(resultPattern)

        #mayores a 1 se convierten en positivo, sino en negativo
        for i in range(aux.shape[0]):
            if aux[i] >= 1:
                aux[i] = 1
            else:
                aux[i] = -1
        
        return aux