"""
Autor: Errandonea Gonzalo, Rodriguez Alex
Año: 2023
"""

from NnHopfield import NnHopfield
from utilities.showReconstructedPatterns import showReconstructedPatterns
from utilities.getPatterns import getPatterns
from utilities.reconstructPatterns import reconstructPatterns


if __name__ == "__main__":
    
    try:
        dirCsv = []
        dirImgs = []

        print('INGRESE LOS DIRECTORIOS DE LOS ARCHIVOS PARA ENTRENAR LA RED DE HOPFIELD')
        optionCsvTrain = input('desea cargar CSVs? (Y/N): ')

        if(optionCsvTrain.upper() == 'Y'):
            csvInput = input("Ingrese los directorios separados por comas (csv): ")
            dirCsv = csvInput.split(',')

        optionsImgTrain = input('desea cargar imagenes? (Y/N): ')

        if(optionsImgTrain.upper() == 'Y'):

            imgsInput = input("Ingrese los directorios separados por comas (imagenes): ")
            dirImgs = imgsInput.split(',')

        print('INGRESE LOS DIRECTORIOS DE LOS ARCHIVOS PARA SER RECONSTRUIDOS POR LA RED DE HOPFIELD')

        optionCsvPredict = input('desea cargar CSVs? (Y/N): ')

        if(optionCsvPredict.upper() == 'Y'):
            csvInputPredict = input("Ingrese los directorios separados por comas (csv): ")
            dirCsvPredict = csvInputPredict.split(',')

        optionsImgPredict = input('desea cargar imagenes? (Y/N): ')

        if(optionsImgPredict.upper() == 'Y'):

            imgsInputPredict = input("Ingrese los directorios separados por comas (imagenes): ")
            dirImgsPredict = imgsInputPredict.split(',')

        if ((optionCsvTrain.upper() == 'Y' or optionsImgTrain.upper() == 'Y')
            and (optionCsvPredict.upper() == 'Y' or optionsImgPredict.upper() == 'Y')):

            hopfield = NnHopfield()

            data = getPatterns(arrPathCsv=dirCsv, arrImgs=dirImgs)

            hopfield.train(data)

            dataPatterns = getPatterns(arrPathCsv=dirCsvPredict, arrImgs=dirImgsPredict)

            listPatterns = reconstructPatterns(dataPatterns, hopfield)

            showReconstructedPatterns(listPatterns)
    except Exception as e:
        print('ERROR, Ocurrio un error inesperado')
        print(e)


    