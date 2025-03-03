import numpy as np
import matplotlib.pyplot as plt

I = np.array([[2,1,0],[1,2,0],[0,0,1]])
print("Matriz no diagonal:")
print(I)
print(I[:,1])

valoresPropios, vectoresPropios = np.linalg.eig(I)

a = valoresPropios
b = vectoresPropios

print("Valores Propios:",a)
print("Vectores Propios:",b)

Orden = np.argsort(valoresPropios)
print(Orden)

DOvalor = a[Orden]
DOvector = b[Orden]
print(DOvalor)
print(DOvector)