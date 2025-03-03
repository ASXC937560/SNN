
# Ecuación de Schördinger con el potencial de Lennard-Jones
#Usamos unidades atómicas
import numpy as np
import matplotlib.pyplot as plt


#Definimos el potencial de Lennard-Jones
def getV(x):
    epsilon = 100
    sigma = 1
    potvalue = 4*epsilon*((sigma/x)**12-(sigma/x)**6)
    return potvalue

#Hacemos la la matriz (discretizamos en n puntos de 0 a n-1), el potencial de Lennard-Jones solo se aplica en los componente i,i
def Eq(n,h,x):
    F = np.zeros([n,n])
    for i in range(0,n):
        F[i,i] = -2*((h**2)*getV(x[i]) + 1)
        if i > 0:
           F[i,i-1] = 1
           if i < n-1:
              F[i,i+1] = 1
    return F


#Creamos el intervalo de nuestro sistema
xlower = 0.75
xupper = 3.5

#Discretización (separación de cada x)
h = 0.02  
#Creamos las coordenadas x donde calcularemos la solución
x = np.arange(xlower,xupper+h,h)
#Tamaño del grid
npoints=len(x) 

print("Using",npoints, "grid points.")

#Calculamos la ecuación de Schrödinger 
print("Calculating matrix...")
F=Eq(npoints,h,x)

#Diagonalizamos la matriz F
print("Diagonalizing...")
eigenValues, eigenVectors = np.linalg.eig(F)

#Ordenamos los resultados a partir de los valores propios
# w son los autovalores ordenados vs son los autovectores ordenados
idx = eigenValues.argsort()[::-1]   
w = eigenValues[idx]
vs = eigenVectors[:,idx]

#El autovalor no es directamente la energia, hacemos esta operación para obtener la energia
E = - w/(2.0*h**2)

#Obtenemos el valor de las energias
print("RESULTS:")
for k in range(0,4):
	print("State ",k," Energy = %.3f" %E[k])
#Hacemos una lista vacia on npoints elements para la función de onda
psi = [None]*npoints

#Calculamos la función de onda normalizada
for k in range(0,len(w)):
	psi[k] = vs[:,k]
    #Aquí hacemos su cuadrado a traves del producto escalar
	integral = h*np.dot(psi[k],psi[k])
    #Normalizmos la función de onda
	psi[k] = psi[k]/integral**0.5

#Hacemos los gráficos de las funciones de onda
print("Plotting")

#Hacemos los gráficos de cada función de onda según el autovalor (energía) que le corresponda
for v in range(0,4):
    plt.plot(x,psi[v],label=r'$\psi_v(x)$, k = ' + str(v))
    plt.title(r'$n=$'+ str(v) + r', $E_n$=' + '{:.2f}'.format(E[v]))
    plt.legend()
    plt.xlabel(r'$x$(a.u.)')
    plt.ylabel(r'$\psi(x)$')
    plt.show()

print("Bye")
