#Crear dos matrices donde la cantidad de filas y columnas serán 3 x 3. Los
#elementos de estas matrices deben ser generados de forma aleatoria (-5 a -10).
#Luego se deben multiplicar ambas matrices e imprimir la matriz resultante.
#Agregar una condición para que las dimensiones sean acordes para realizar la
#multiplicación entre ambas matrices
import numpy as np
#Matrices
m1=np.random.randint(-10,-5,(3,3))
m2=np.random.randint(-10,-5,(3,3))
print("MATRIZ 1: ")
print(m1)
print("MATRIZ 2: ")
print (m2)
#Multiplicacion de Matricez
mr=m1*m2
print("MATRIZ RESULTANTE 1: ")
print(mr)
#Matriz identidad
mi=([1,0,0],    
[0,1,0],
[0,0,1])
#Multiplicacion por M.Identidad
mrf=mi*mr
print(mrf)