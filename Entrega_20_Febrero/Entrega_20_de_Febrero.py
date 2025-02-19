#Ejemplo de caída libre

#Importo la libreria matemática (numpy) y la de hacer gráficas matplotlib
import numpy as np
import matplotlib.pyplot as plt

u_list = [1,2,3]
#Defino X para hacer la trayectoria a traves de elejir la velocidad como input
def draw_trajectory(v,u):

    #Defino la aceleración de la gravedad en m/s^2   
    g = 9.8

    #Defino el tiempo total de vuelo que tendrá
    t_flight = 2*v/g

    #A partir del tiempo total de vuelo creo los intervalos para poder hacer la gráfica
    intervals = np.arange(0, t_flight, 0.001)

    #Creo una lista vacia para las coordenadas X y Y (la X es para que no se solapen y poder distinguir bien las 3 trayectorias)
    x = []
    y = []
    
    #Hago un loop a través del tiempo para calcular las coordenadas (en concreto solo Y)   
    for t in intervals:
        x.append(u)
        y.append(v*t-0.5*g*t*t)
        
    #Genero el gráfico y le añado título y coordenadas X y Y con unidades
    plt.plot(x,y)
plt.xlabel('Puntos de separación')
plt.ylabel('Height (m)')
plt.title('Projectile motion')
plt.xticks(u_list)
#Genero la lista de velocidades iniciales m/s
v_list = [20, 40, 60]

for v,u in zip(v_list,u_list):
    draw_trajectory(v,u)

    #Calculo la altura máxima respecto a cada velocidad inicial
    g = 9.8
    print("Altura máxima de  velocidad",v)
    ymax = (v*v/g)-0.5*g*(v/g)*(v/g)
    print(ymax)

    #Calculo el tiempo de vuelo para cada velocidad
    print("Tiempo de vuelo de cada velocidad",v)
    t_flight = 2*v/g
    print(t_flight)

#Muestra la gráfica con una leyenda
plt.legend(['20', '40', '60'])
plt.show()