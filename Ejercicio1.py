#Obtener la determinante de una matriz de 3 x 3 con sus elementos aleatorios (5
#al 10, enteros positivos). Se pueden utilizar librerías para resolver el algoritmo.

import numpy as np
#Crear Matriz   
m=np.random.randint(5,10,(3,3))
print(m)
#Calcular determinante de la matriz
deter=np.linalg.det(m)
print(deter)