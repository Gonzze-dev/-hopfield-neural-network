"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

import numpy as np

from utilities.convertToVectorBipolar import convertToVectorBipolar

class Hopfield():

    def __init__(self):
        #Matriz de pesos
        self.weight = []

    def _activation(self, genericFunction=convertToVectorBipolar, *args):
        """
        Esta funcion recibe una funcion X con K cantidad de argumentos
        Hecha para reconvertir de forma facil el vector sin tener que hacer cambios a la
        libreria
        """
        return genericFunction(args)

    def train(self, patternsArr):
        """
            Esta funcion recibe un array de patrones de mismo tamaño N
            ejemplo: hp.train([[-1,-1,1,-1], [1,1,1,-1]])
            el tamaño de patrones determinara la cantidad de neuronas

            Return
            Retorna la matriz de pesos
        """
        #obtener el tamaño del patron
        lenPatterns = len(patternsArr[0])

        #inicializo la matriz cuadrada con el mismo tamaño que los vectores columna 
        #de pesos en ceros
        self.weight = np.zeros((lenPatterns,lenPatterns))

        for pattern in patternsArr:
            #Copia los elementos de la matriz, para no mutar elementos por referencia
            vecCol = [np.copy(pattern)]
            #Hago la transpuesta del vector columna
            vecRow = np.transpose(vecCol)
            #multiplico el vector fila por el vector columna
            resultWeight = vecRow @ vecCol
            #sumamos las matrices de pesos
            self.weight = self.weight + resultWeight
        
        #convertirmos su diagonal en ceros
        np.fill_diagonal(self.weight, 0)

        return self.weight
    
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
        countIterations = 0
        
        #Copia los elementos de la matriz, para no mutar elementos por referencia
        result = np.copy(pattern)

        oldResult = None

        #Mientras el anteultimo resultado no sea igual al resultado obtenido
        #seguira iterando hasta que sean iguales
        
        #********A IMPLEMENTAR************
        #Poner a su vez un limite maximo (NUMERO EPOC)
        #********A IMPLEMENTAR************
        while(not np.array_equal(oldResult,result) and countIterations <= maxIterations):
            oldResult = np.copy(result)

            #multiplico el vector columna que es el patron del resultado anterior
            #por la matriz de pesos
            result = oldResult @ self.weight

            #conveirto elementos
            #mayores a 1 se convierten en positivo, sino en negativo
            result = self._activation(genericAlgorithm, result)

            countIterations += 1

        return result, countIterations