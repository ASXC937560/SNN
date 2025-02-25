
# Movimiento armonico simple con k/m =1



import numpy as np
import matplotlib.pyplot as plt
#Me invento un valor de m y k pero que mantengan k/m=1
m = 10.0
k = 10.0
#Condiciones iniciales
x0 = 0.1
v0 = 0.0
#Calculo la energia inicial (con las condiciones iniciales)
E0 = (m/2.0)*v0*v0+(k/2)*x0*x0

print('\n--------------------------------------------------------')
print('SIMPLE MD SIMULATION OF A SINGLE PARTICLE IN HARMONIC TRAP')
print('----------------------------------------------------------')

#Input de cada paso
dt = 0.0001
#Tiempo final
ntot = 100000
#Los numeros son exagerados pero es para asegurar el resultado de los gráficos
print('Simulation time will be',dt*ntot,' sec')

#Hago un array vacio de posición,velocidad,tiempo,velocidad media (v2), velocidad de medio salto (v_hk), energia y RE (relación de la energia respecto a la energia inicial)
x = np.zeros(ntot+1)
v = np.zeros(ntot+1)
t = np.zeros(ntot+1)
v2 = np.zeros(ntot+1)
v_hk = np.zeros(ntot+1)
E = np.zeros(ntot+1)
RE = np.zeros(ntot+1)
#Añado las condiciones iniciales en 0.0
t[0] = 0.0
x[0] = x0
v[0] = v0
v2[0] = 0.0
E[0] = E0
RE[0] = 1

#Calculo la aceleración y velocidad despues de dt/2
a = -x[0]
v_hk[0] = v[0]+(dt/2.0)*a
#Calculo la nueva posición y hago t+dt 
x[1] = x[0]+dt*v_hk[0]
t[1] = t[0]+dt
#Calculo la aceleración en el punto 1 para calcular el v_hk en el siguiente dt/2 (damos de tiempo dt)
a = -x[1]
v_hk[1] = v_hk[0]+a*dt
v2[1]=(v_hk[1]+v_hk[0])/2 #Opcional pero lo pongo para tener la idea de como se calcula las velocidades en los sitios que también estan las posiciones calculadas 
i=1

print('\n Calculating time evolution...')
while i<ntot:
	#Calculo la aceleración en la posición i
    a = -x[i]
    #Calculo la nueva posición
    x[i+1] = x[i]+dt*v_hk[i]
    #Calculo la nueva velocidad de dt/2 haciendo dt
    v_hk[i+1] = v_hk[i]+a*dt
    #Calculo la velocidad que esta en el mismo tiempo que las posiciones que calculamos, es a traves de la media
    v2[i]=(v_hk[i+1]+v_hk[i])/2
    #Calculo las energias en esas posiciones
    E[i] = (m/2.0)*v2[i]*v2[i]+(k/2)*x[i]*x[i]
    #Hago la relación de la energia calcula de antes respecto a la inical
    RE[i] = E[i]/E0
    t[i+1] = t[i]+dt
    #Vemos el paso y sus correspondientes posiciones,tiempos, velocidades, energias y relacion de energia respecto a la inicial
    print('Step',i,' t= ',round(t[i],3),' x=',round(x[i],3),"v2=",round(v2[i],3),"E=",round(v2[i],3),"RE=",round(v2[i],3))
    i=i+1
#Lo mismo que la línia 71, pero se ve que el último punto no tiene sentido ya que al no poder calcular v2, coge v2 igual a 0 debido al array de ceros del inicio, dando RE=0
print('Final Step', i,' t= ',round(t[i],3),' x=',round(x[i],3),"v2=",round(v2[i],3),"RE=",round(v2[i],3))
print('\nShowing plot with results')

plt.figure(1)

plt.subplot(211)
plt.plot(t,x)
plt.ylabel('x (nm)')

plt.subplot(212)
plt.plot(t[:ntot],v2[:ntot])
plt.ylabel(' v (nm/ns)')
plt.xlabel('time (ns)')

plt.show()


#Hago el gráfico para ver que se conserva la energia (da 1), el último punto no cuadra pero esto ocurre ya que no puedo calcular el v2 acorde a esa posición.
plt.plot(t,RE,'k')
plt.xlabel('time (ns)')
plt.ylabel('E/E0')

plt.show()


