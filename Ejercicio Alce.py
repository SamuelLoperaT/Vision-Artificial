import cv2
import numpy as np
import matplotlib.pyplot as plt

#lectura de la imagen desde un directorio en windows, en mac o en linux el formato de archivo es distinto
img = cv2.imread(r"C:\Users\samue\Documents\Resources\alce.png", cv2.IMREAD_COLOR)
#correccion de canal de color de BGR a RGB
img_corr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#creacion de los cuadrantes

#cuadrante 1 toma todos los colores y hace referencia a la esquina superior izquierda}
img_slice_1 = img_corr[0:143, 0:194]
#cuadrante 2 toma el verde y hace referencia a la esquina inferior izquierda
img_slice_2 = img_corr[0:143, 194:388, 1]
#cuadrante 3 toma el rojo y hace referencia a la esquina inferior derecha
img_slice_3 = img_corr[143:286, 194:388, 0]
#cuadrante 2 toma el azul y hace referencia a la esquina superior derecha
img_slice_4 = img_corr[143:286, 0:194, 2]


#creacion de matriz en ceros con el mismo tipo de datos y tamaño de la imagen original
img_modified = np.zeros(np.shape(img_corr), dtype=np.uint8)

#asignacion de datos del cuadrante 1 en formato BGR
img_modified[0:143, 0:194, 0] = img_slice_1[:,:,2]
img_modified[0:143, 0:194, 1] = img_slice_1[:,:,1]
img_modified[0:143, 0:194, 2] = img_slice_1[:,:,0]

#asignacion de datos del cuadrante 2 en formato BGR (los 0 hacen referencia a que no se toma el color referenciado)
img_modified[0:143, 194:388, 0] = img_slice_2[:,:]
img_modified[0:143, 194:388, 1] = 0
img_modified[0:143, 194:388, 2] = 0

#asignacion de datos del cuadrante 3 en formato BGR (los 0 hacen referencia a que no se toma el color referenciado)
img_modified[143:286, 194:388, 0] = 0
img_modified[143:286, 194:388, 1] = 0
img_modified[143:286, 194:388, 2] = img_slice_3[:,:]

#asignacion de datos del cuadrante 4 en formato BGR (los 0 hacen referencia a que no se toma el color referenciado)
img_modified[143:286, 0:194, 0] = 0
img_modified[143:286, 0:194, 1] = img_slice_4[:,:]
img_modified[143:286, 0:194, 2] = 0

#correccion de canal de color de la imagen modificada, de formato BGR a RGB
img_modified = cv2.cvtColor(img_modified,cv2.COLOR_BGR2RGB)

#mostrar (display)  la imagen, plt.show() se pone para asegurar que tras leer la imagen si se presente por fuera de ides que no tienen integracion para matplotlib
plt.imshow(img_modified, cmap = 'gray')
plt.show()
