"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from csv import reader

def readCsv(file):
    """
        Se ingresa el path del csv, lo lee, convierte cada numero a
        tipo float

        Ejemplo
        readCsv('nombreCarpeta/miCsv.csv')

        Return
        Matriz donde se encuentran los elementos del csv,
        los elementos se convierten en tipo float

        O

        None, si no se encuentra el archivo y se imprime el error

        O
        None, si ocurre un error inesperado y se imprime el error
    """

    try:
        dataList = []
        with open(file, newline='') as fileCsv:
            dataCsv = reader(fileCsv)

            for data in dataCsv:
                validData = [float(element) for element in data if element.strip()]  # Verifica si el elemento contiene datos
                if validData:
                    dataList.append(validData)

        return dataList
    
    except FileNotFoundError as e:
        
        print(f"Error: El archivo '{file}' no existe.")
        print(e)
        return None
    except Exception as e:

        print(f"Ocurrio un error inesperado: ", e)
        print(e)
        return None