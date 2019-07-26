from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 0.1

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.02

def func (conds, t, g ): # funcion definida para los valores de theta y omega (Reducimos el grado de la ecuación)
    dthe = conds[1] #Derivada de theta
    dr=conds[3]     #Derivada de l
    dome=-(2*conds[3]*conds[1])/conds[2]-(g/conds[2])*sin(conds[0])
    ddr=(conds[2])*(conds[1])**2-(k/m)*(conds[2]-b)-g*cos(conds[0])
    return array([dthe, dome, dr, ddr], float)

#Condiciones iniciales-----------------------------------------------------------------
g = 9.81
b=0.01
k=1
m=1
thes = 60*pi/180.
l=0.1
omes = 0.
r=0.2


initcond = array([thes,omes,l,r], float)#arreglos de las condiciones iniciales

n_steps = 1000 #numero de pasos
t_start = 0. #tiempo inicial
t_final = 4.#tiempo final
t_delta = (t_final - t_start) / n_steps #diferencial de tiempo
t = linspace(t_start, t_final, n_steps)#arreglo de diferencial de tiempo

solu, outodeint = odeint( func, initcond, t, args = (g,), full_output=True) #solucion de la ecuacion diferencial (parametros acordes a los definidos en la funcion)

theta, omega, ll, rr = solu.T # solucion para cada paso de theta y omega



# =====================

scene.range = 0.6 # tamaño de la ventana de fondo

xp = l*sin(thes) #pasa de coordenadas polares a cartesinas
yp = -l*cos(thes)
zp = 0.

sleeptime = 0.0001 # tiempon con el que se utiliza la posicion de la particula

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.yellow) #Definimos la esfera

time_i = 0 #es un contador que se mueve ene el espacio temporal en donde se resolvio la ecuacion deferencial
t_run = 0 #tiempo en el q se ejecuta la animacion

#for i in omega:
#    print(i)


while t_run < t_final: #animacion 
    sleep(sleeptime) 
    prtcl.pos = vector( ll[time_i]*sin(theta[time_i]), -ll[time_i]*cos(theta[time_i]), zp )
    
    t_run += t_delta
    time_i += 1
