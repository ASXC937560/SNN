#Ejemplo de caída libre

#Importo la libreria matemática (numpy) y la libreria de graficar (matplotlib) 
import numpy as np
import matplotlib.pyplot as plt

#Lista que servirá para separar en X las 3 trayectorias a graficar
u_list = [1,2,3]
#Defino una función para hacer la trayectoria, la v es la velocidad y la u es para poder separar las diferentes caídas libres en X
def draw_trajectory(v,u):

    #Defino la aceleración de la gravedad en m/s^2   
    g = 9.8

    #Defino el tiempo total de vuelo en s
    t_flight = 2*v/g

    #A partir del tiempo total de vuelo creo los intervalos para poder hacer la gráfica
    intervals = np.arange(0, t_flight, 0.001)

    #Creo una lista vacia para las coordenadas X y Y (la X es para que no se solapen y poder distinguir bien las 3 trayectorias)
    x = []
    y = []
    
    #Hago un loop a través del tiempo para calcular la coordenada Y, en X solo está el termino que separa trayectorias (u)
    for t in intervals:
        x.append(u)
        y.append(v*t-0.5*g*t*t)
        
    #Genero el gráfico, le añado título y coordenadas X y Y (con unidades), por último hago que en la X hago que solo esten marcados los valores de la u_list
    plt.plot(x,y)
plt.xlabel("Puntos de separación")
plt.ylabel("Height (m)")
plt.title("Projectile motion")
plt.xticks(u_list)

#Lista de velocidades iniciales m/s
v_list = [20, 40, 60]
#Itero las velocidades iniciales y la separación de las distintas caídas libres
for v,u in zip(v_list,u_list):
    draw_trajectory(v,u)

    #Calculo la altura máxima respecto a cada velocidad inicial
    g = 9.8
    print("Altura máxima de velocidad",v)
    ymax = (v*v/g)-0.5*g*(v/g)*(v/g)
    print(ymax)

    #Calculo el tiempo de vuelo para cada velocidad inicial
    print("Tiempo de vuelo de velocidad",v)
    t_flight = 2*v/g
    print(t_flight)

#Muestra la gráfica con una leyenda
plt.legend(["20", "40", "60"])
plt.show()