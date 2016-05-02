
# coding: utf-8

# In[10]:

#Bibliotecas utilizadas
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------
#Definimos las constantes 
#Valor de la gravedad
g=9.8        
#Longitud de la cuerda
l=0.5  

#Periodo base
T0=2*np.pi*np.sqrt(l/g)

#Que tan tupido esta el intervalo
n=1000
#Error añadido para que no divida entre 0
e=0.0001
#Rango de theta0 
theta0=np.linspace(e,(np.pi)+e,n) 

#------------------------------------------
#Defino los arrays para todos los resultados arrojados
S=[0 for i in range(n)]
TT=[0 for i in range(n)]
R=[0 for i in range(n)]
T=[0 for i in range(n)]
real0=[0 for i in range(n)]
real2=[0 for i in range(n)]
real4=[0 for i in range(n)]
real6=[0 for i in range(n)]
real8=[0 for i in range(n)]

#------------------------------------------
#Con un doble loop para poder considerar los casos
#donde se agregan mas terminos de la serie de potencias

#Paso a paso con los términos porque no se hacer multigraficas
M0=0

#Comienzo un loop para poder calcular todos los resultados 
#posibles contemplando un angulo inicial variante
for i in range(M0):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real0[j]=(T[j]/T0)
#------------------------------------------        
M2=2
for i in range(M2):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real2[j]=(T[j]/T0)-1
#------------------------------------------        
M4=4
for i in range(M4):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real4[j]=(T[j]/T0)-2
#------------------------------------------
M6=6
for i in range(M6):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real6[j]=(T[j]/T0)-3
#------------------------------------------
M8=8
for i in range(M8):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real8[j]=(T[j]/T0)-4

#------------------------------------------
#Para la grafica
plt.plot(theta0, real0, 'y', label="T0")
plt.plot(theta0, real2, 'm', label="T2")
plt.plot(theta0, real4, 'r', label="T4")
plt.plot(theta0, real6, 'b', label="T6")
plt.plot(theta0, real8, 'g', label="T8")
plt.title('Error using power series')
plt.grid()
plt.xlabel('Angle')
plt.xlim(0,np.pi)
plt.ylabel('Error')
plt.legend(loc='best')

#Pa' guardar la foto sin problemas
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.5,5.5)
fig.savefig('error.png',dpi=100)


