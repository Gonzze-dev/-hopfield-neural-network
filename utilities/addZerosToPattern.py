"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from numpy import concatenate, zeros

def addZerosToPattern(pattern, numNeurons):
    """
        Verificamos que el tamaño del patron sea igual al numero de neuronas
        Si no es asi, entonces si es menor se agregan ceros
        Si es igual, restorna el valor por defecto
        Si es mayor, entonces lanza un error

        Ejemplo
        verifyPattern([1,1,1], 4)

        Return
        
        retorna un vector con 
        tamaño del vector original + numero de neuronas faltantes
    """
    
    lenPattern = len(pattern)
    
    if lenPattern < numNeurons:
        zeroMissings = numNeurons - lenPattern
    
        # Agregar ceros al final del vector
        pattern = concatenate((pattern, zeros(zeroMissings)))
    elif lenPattern > numNeurons:
        rangePatternIsGraterOfNumNeurons = (f"El patron no puede ser mas grande que el numero de neuronas:" 
                        +  f"\nTamaño del patron: {str(lenPattern)}"
                        + f"\nNumero de neuronas: {str(numNeurons)}")
        
        raise ValueError(rangePatternIsGraterOfNumNeurons)

    return pattern