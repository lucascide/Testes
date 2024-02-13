import numpy as np

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1,2]])

print("Soma das matrizes: " + str(X + Y))
print("Multiplicação de X por escalar: " + str(4 * X))
print("Multiplicação de elementos de X por Y: " + str(X * Y)) # Hadamard product
print("Multiplicação de X por Y: " + str(np.dot(X, Y)))
print("Matriz transposta de X: " + str(X.T)) 

A = np.array([[1,2],[3,4],[5,6],[7,8]])

B = np.array([[1,2,3],[4,5,6],[7,8,9]])
