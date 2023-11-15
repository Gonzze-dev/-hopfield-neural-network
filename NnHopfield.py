"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from Hopfield import Hopfield

from utilities.convertToVectorBipolar import convertToVectorBipolar
from utilities.addZerosToPattern import addZerosToPattern
from utilities.verifyElementsOfPattern import verifyElementsOfPattern

from numpy import array
#Clase creada para manejar errores
class NnHopfield(Hopfield):
    def __init__(self):
        super().__init__()

    def train(self, patternsArr):
        """
        Esta funcion recibe un array de patrones de mismo tamaño N
        ejemplo: hp.train([[-1,-1,1,-1], [1,1,1,-1]])
        el tamaño de patrones determinara la cantidad de neuronas

        Return
        Retorna la matriz de pesos
        """
        try:
            
            for pattern in patternsArr:
                verifyElementsOfPattern(pattern)

            
            lenMax = len(max(patternsArr, key=len))

            for i in range(len(patternsArr)):
                patternsArr[i] = addZerosToPattern(patternsArr[i], lenMax)

            return super().train(patternsArr)
        except Exception as e:
            print(f"Se produjo un error: {e}")
    
    def predict(self, pattern, genericAlgorithm=convertToVectorBipolar, maxIterations=20):
        """
        Intenta recuperar el patron dado.
        Esta funcion permite recibir como parametro (opcionalmente) 
        una funcion de activacion cual se quiera.
        Igual que la cantidad maxima de iteraciones.

        Ejemplo:
        predict([1,1,1,1])

        predict([1,1,1,1], genericAlgorithm=activationFunction)

        predict([1,1,1,1], genericAlgorithm=activationFunction, maxIterations=10)

        Return
        Retorna el patron reconstruido y la cantidad de iteraciones hechas
        """
        
        try:
            pattern = addZerosToPattern(pattern, self.weight.shape[1])

            result, iters = super().predict(pattern, genericAlgorithm, maxIterations)

            return result, iters
        except Exception as e:
            print(f"Se produjo un error: {e}")