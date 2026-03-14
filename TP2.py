import numpy as np

a = np.array([1, 42, 18])
b = np.arange(10)
c = np.arange(2, 5, .5)
c = np.linspace(0, 1, 11)
d = np.ones(6)
d = np.zeros(5)
e = np.full(5, 3)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array(([1, 2, 3, 4, 5, 6, 7, 8, 9])).reshape((3, 3))
C = np.ones((2, 5))

# print(f"Dimensão A: {A.ndim}, Tamanho A: {A.size}, Forma A: {A.shape}")

t1 = np.concatenate((a, b))
t2 = np.vstack((A, a))
t3 = np.hstack((A, A))

t4 = e**d
# print(t4)

# print(A)
# print(A.sum(axis=1)) # retorna uma array com a soma das linhas enqto o 0 retorna a soma das colunas (array tbm)


#Question 1

a1 = np.arange(72)
a1 = a1%2
a1 = a1.reshape(8,9)
a1 = a1.T
a1 = a1[0:8]

#print(a1)

#Question 2

M = np.arange(20)
M = M+1
M = M.reshape(5,4)
M = M.T

#extraindo submat

aux = np.array([True, True, True, False])
M = M[aux]
M = M.T
aux2 = np.array([False, True, True, False, True])
M = M[aux2]
M = M[[0,2,1]]
M = M.T
M = M[[1,2,0]]


#Section 2

import matplotlib.pyplot as plt

x = np.linspace(0, 4, 10)
y = np.sin(x)

# plt.plot(x,y)

# x = np.linspace(0, 10, 1000)
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))

plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.title("une courbe sinusoÃ¯dale")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.show()
