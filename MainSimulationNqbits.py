import math
import numpy as np
from QuantumPackage import getSci
from QuantumPackage import getInitialState
from QuantumPackage import getHamiltonian
import matplotlib.pyplot as plt
import scipy.linalg as scl
import time

start_time = time.time()

#Variables
Nspins = 5
j = 13
Bz = 5
hbar = 1

# Matrices
Sx = np.matrix([[0,1],[1,0]])   
Sz = np.matrix([[1,0],[0,-1]])
I = np.matrix([[1,0],[0,1]])

# Hamiltonianio
H = getHamiltonian(j,Bz,Nspins,Sx,Sz)


# Condicion inicial
X = np.matrix([[1],[-1]])/math.sqrt(2)
Psi_0 = getInitialState(X,Nspins)


# Tiempo
ti = 0
tf = 15/Bz
N = 1000
dt =(tf-ti)/(N)
t = np.arange(ti,tf,dt)


# Funcion de onda inicial 
psi = Psi_0

# Magnetizacion promedio en x y z
Mx = 0
Mz = 0

# Inicialización operadores de magnetizacion
for i in range(1,Nspins+1):
    Sxi = getSci(Sx,i,Nspins)
    Szi = getSci(Sz,i,Nspins)
    Mx = Mx + Sxi/Nspins
    Mz = Mz + Szi/Nspins


# Coeficientes function de onda
c1 = np.zeros([1,N], dtype=np.complex_)
c2 = np.zeros([1,N], dtype=np.complex_)
c3 = np.zeros([1,N], dtype=np.complex_)
c4 = np.zeros([1,N], dtype=np.complex_)

# Magnetizacion promedio
PromMx = np.zeros([1,N], dtype=np.complex_)
PromMZ = np.zeros([1,N], dtype=np.complex_)

# Operador evolucion temporal
U = scl.expm(-1j*H/hbar*dt)

# Simulacion de la ecuacion de Schrodinger
for n in range(0,N):
    if n == 0:
        psi = Psi_0
        PromMx[0][n] = psi.getH() * Mx * psi
        PromMZ[0][n] = psi.getH() * Mz * psi
    else:
        psi =  U*psi

        PromMx[0][n] = psi.getH() * Mx * psi 
        PromMZ[0][n] = psi.getH() * Mz * psi


    
# Funciones temporales para la magnetizacion
MeanMz = PromMZ[0][:]
MeanMx = PromMx[0][:]


lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(t*Bz, MeanMz,'-r', linewidth=3); 
plt.ylabel(r'$\langle M_z \rangle$');plt.xlabel(r'$B_z t$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0, tf*Bz)
plt.savefig('Mz.png')

lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(t*Bz, MeanMx,'-b', linewidth=3); 
plt.ylabel(r'$\langle M_x \rangle$');plt.xlabel(r'$B_z t$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0, tf*Bz)
plt.savefig('Mx.png')

print('Bz : ', Bz)
print('j : ', j)
print('t : ', t)
print("--- %s seconds ---" % (time.time() - start_time))