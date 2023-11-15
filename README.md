# Red de Hopfield

Este código implementa una red neuronal de Hopfield para la recuperación de patrones. Permite convertir los datos a formatos binarios o bipolares. El uso de esta librería es público y está disponible para su utilización.

## Autores

Esta librería fue desarrollada por:

- Errandonea Gonzalo
- Rodriguez Alex

## Requisitos

Para utilizar el código completo, se requiere la instalación de las siguientes dependencias:

- Python 3.12.0
- Numpy 1.26.2
- Scikit-image (skimage) 0.22.0

## Instalación

No es necesario realizar una instalación especial, solo asegúrate de tener Python instalado junto con las dependencias mencionadas (Numpy y Scikit-image).

```
pip install numpy==1.26.2
pip install scikit-image==0.18.1
```

## Uso

El programa no cuenta con una interfaz gráfica y debe ser ejecutado desde una terminal.

Para utilizar la clase `hopfield`, se necesita únicamente la librería Numpy y el módulo `convertToVectorBipolar`.

Para usar la clase `NnHopfield`, se requiere la clase `hopfield` y los módulos `verifyElementsOfPattern`, `addZerosToPattern` y `convertToVectorBipolar`. Todos estos módulos se pueden encontrar en la carpeta 'Utilities'.
Puedes instalar estas dependencias usando pip:

## Ejecución del `main.py`

1. Prepara los directorios que contienen archivos CSV o imágenes para entrenar la red y para los datos que deseas reconstruir.
2. Ejecuta el programa.
3. Ingresa los directorios de los archivos CSV para entrenar la red.
4. Ingresa los directorios de las imágenes para entrenar la red.
5. Ingresa los directorios de los archivos CSV para recuperar datos distorsionados.
6. Ingresa los directorios de las imágenes distorsionadas que se desean recuperar.
7. Se mostrará un plot con los datos recuperados representados en gráficos.

## Informe de Ejecución de Algunos Tests

### Test 3

- Se obtienen datos del archivo CSV "data.csv".
- Se entrena la red.
- Se intenta recuperar un patrón distorsionado.

### Test 6

- Se convierten una serie de imágenes a patrones.
- Se entrena la red.
- Se lee una imagen con la que se entrenó la red y se corrompe.
- Se convierte a un patrón.
- Se intenta recomponer la imagen.
- Se imprimen las iteraciones y se muestra el patrón vector convertido en una matriz en un plot.

### Test 7

- Se convierte una serie de imágenes a patrones, pero esta vez las imágenes se tratan del mismo objeto.
- Se entrena la red.
- Se lee una imagen con la que se entrenó la red y se corrompe dicha imagen.
- Se convierte en un patrón.
- Se intenta recomponer la imagen.
- El patrón de la imagen a recomponer se convierte en una matriz.
- Se imprimen las iteraciones y el patrón vector que se pasó a un patrón matriz se muestra en un plot.

### Test 8

- Entrena la red con 3 imágenes similares.
- Luego se corrompen las imágenes.
- Se reconstruyen las imágenes corrompidas.
- Se muestran las imágenes en forma de patrón original, corrompido y reconstruido.

### Test 9

- Entrena la red con 2 imágenes similares.
- Luego se corrompen las imágenes, además de una similar a las otras pero que no fue utilizada para entrenar la red.
- Se reconstruyen las imágenes corrompidas.
- Se muestran las imágenes en forma de patrón original, corrompido y reconstruido.
- Este test se realiza para evaluar qué tan buena es la red reconstruyendo imágenes similares que no conoce.

## Evaluación de Resultados

Tras las pruebas realizadas, se concluyó que la red de Hopfield es efectiva para la memorización y asociación de datos, pero tiene limitaciones con grandes volúmenes de datos. Asimismo, la red no puede reconstruir datos que no conoce, por lo que no es óptimo utilizarla si los datos a recuperar no están en un contexto similar a los datos de entrenamiento.

## Información Adicional

- **Año:** 2023
- **Materia:** Inteligencia Artificial
- **Profesor/a:** Dra. Daniela López De Luise

## Repositorio
-link: [Red-de-hopfield-git](https://github.com/Gonzze-dev/-hopfield-neural-network)

## Presentacion
-link: [Canvas-hopfield](https://www.canva.com/design/DAFzz4-q22s/uIvaKSJxko0gciSokzr1mg/edit)

## Contacto

- **Errandonea Gonzalo**
  - Correo: errandoneagonzalo18@gmail.com
  - Github: [Gonzze-dev](https://github.com/Gonzze-dev)

- **Rodriguez Alex**
  - Correo: alekeyn1999@gmail.com
  - Github: [AlexRodriguezZA](https://github.com/AlexRodriguezZA)
  - Linkedin: [alex-rodriguez-zamora](https://www.linkedin.com/in/alex-rodriguez-zamora/)

- **Daniela Lopez De Luise**
  - Correo: lopezdeluise.daniela@uader.edu.ar
  - Linkedin: [Daniela LopezDeLuise](https://www.linkedin.com/in/daniela-lopezdeluise-a973047/)