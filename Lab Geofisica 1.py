
# coding: utf-8

get_ipython().run_line_magic('pylab', 'inline')
import numpy as np
import math

####Punto A

G=6.67e-11
pi=np.pi
roS=2700
roE=4000


x=linspace(-50,50,501) #crea un arreglo


def funcionG(r,z):
    g=(4/3)*pi*G*(r**3)*(roE-roS)*(z/((x**2+z**2)**(3/2)))
    return g

####Punto B

#graf 2
z1=20
r=3
y1=funcionG(r,z1)
plt.plot(x,y1)
max(y1)
#graf 2
z2=30
y2=funcionG(r,z2)
plt.plot(x,y2)
#graf 3
z3=40
y3=funcionG(r,z3)
plt.plot(x,y3)
plt.title("g vs x")
plt.xlabel("x (m)")
plt.ylabel("g (m/s^2)")


####Punto C

#Max g1 medio
mitad1=max(y1)/2
#Max g2 medio
mitad2=max(y2)/2
#Max g3 medio
mitad3=max(y3)/2

y1_restado=abs(y1-mitad1)
min(y1_restado)

####Punto D
x_domo=[0, 700, 1360, 1940, 2420, 2840, 3500, 4080, 5060, 5840]
g_rel=[-1.84e-6, -3.42e-6, -6.67e-6, -1.23e-5, -1.92e-5, -2.39e-5, -2.04e-5, -1.2e-5, -4.33e-6, -2.12e-6]
