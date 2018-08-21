
# coding: utf-8

# In[21]:


get_ipython().run_line_magic('pylab', 'inline')
import numpy as np
import math


# In[41]:


G=6.67e-11
pi=np.pi
roS=2700
roE=4000


# In[56]:


x=linspace(-50,50,1001) #crea un arreglo


# In[57]:


def funcionG(r,z):
    g=(4/3)*pi*G*(r**3)*(roE-roS)*(z/((x**2+z**2)**(3/2)))
    return g


# In[78]:


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


# In[89]:


#Max g1 medio
mitad1=max(y1)/2
#Max g2 medio
mitad2=max(y2)/2
#Max g3 medio
mitad3=max(y3)/2

y1_restado=y1-mitad1
if y1_restado==0:
    


# In[92]:


for i in range (min(x),max(x)):
    if y1==mitad1:
        print (x[i])
    i+=1

