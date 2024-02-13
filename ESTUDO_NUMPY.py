import numpy as np

# a = np.array([0, 1, 2, 3, 4])

# print(a.size)
# print(a.ndim)  # Numero de dimensoes
# print(a.shape) # Indica o tamanho do array em cada dimensão em forma de tupla

## Slicing (É um intervalo do tipo [0,1[)

# a[0:2] = 7, 9


# # Soma vetorial

# u = np.array([0, 1])
# v = np.array([1, 0])

# sumUV = u + v
# difUV = u - v
# scalar_multiplication_u = 2*u
# product_uv = u*v
# dot_product_uv = np.dot(u, v)
# print("Soma de dois vetores = " + str(sumUV))
# print("Produto de vetor por um escalar = " + str(scalar_multiplication_u))
# print("Produto entre u e v = " + str(product_uv))
# print("Produto escalar entre u e v = " + str(dot_product_uv))

# # Broadcasting (Adicionar um escalar a cada valor do vetor):

# print(u+1)

### Universal functions ###

a = np.array([1, -1, 1, -1])
mean_a = a.mean()
max_a = a.max()

print("Media de a = " + str(mean_a))
print("Maior elemento de a = " + str(max_a))

np.pi
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x) # Aplica a função seno a cada elemento do array
print(np.linspace(-2, 2, num=9)) # Faz um espaçamento igual de 9 numeros com inicio em -2 e fim 2em 2

# Plotando um grafico seno:

dominio = np.lipspace(0, 2*np.pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.plot(x, y)

