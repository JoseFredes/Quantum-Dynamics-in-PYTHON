import math
import numpy as np
from numpy.core.numeric import identity
from math import sqrt
from getSci import getSci
import matplotlib.pyplot as plt
from getconjugated import  getTconjugated

#variables
Nspins = 2
j = 13
Bz = 5
hbar = 1

#matrices
Sx = np.array([[0,1],[1,0]])
Sz = np.array([[1,0],[0,-1]])
I = np.identity(2)

#hamiltonianio
H = -j * np.kron(Sx,Sx) - Bz * (np.kron(Sz,I)+np.kron(I,Sz))

#condicion inicial
RightState = np.transpose([1,1])/math.sqrt(2)
Psi_0 = np.kron(RightState,RightState)


#tiempo
ti = 0
tf = 15/Bz
N = 1000
dt =(tf-ti)/(N-1)
t = np.arange(ti,tf,dt)

#dinamica 
psi = Psi_0

#magnetizacion
Mx = 0
Mz = 0

for i  in (1,Nspins):
    Sxi = getSci(Sx,i,Nspins)
    Szi = getSci(Sz,i,Nspins)
    Mx = Mx + Sxi / Nspins
    Mz = Mz + Szi / Nspins

#funciones
c1 = np.zeros(1,N)
c2 = np.zeros(1,N)
c3 = np.zeros(1,N)
c4 = np.zeros(1,N)
PromMx = np.zeros(1,N)
PromMZ = np.zeros(1,N)

# for n in range(1,N):
#     if n == 1:
#         psi = Psi_0
#         c1(n) = psi(1)
#         c2(n) = psi(2)
#         c3(n) = psi(3)
#         c4(n) = psi(4)
#         PromMx(n) = np.transpose(psi) * Mx * psi
#         PromMZ(n) = np.transpose(psi) * Mz * psi
#     else:
#         psi =  math.expm(-1*i*H/hbar*dt)*psi
    

#     #componentes de la funcion de onda
#     c1(n) = psi(1)
#     c2(n) = psi(2)
#     c3(n) = psi(3)
#     c4(n) = psi(4)
#     PromMx(n) = np.conj().transpose(psi)*Mx*psi 
#     PromMZ(n) = np.conj().transpose(psi)*Mz*psi

#     #probabilidades
#     p1 = abs(c1)**2
#     p2 = abs(c2)**2
#     p3 = abs(c3)**2
#     p4 = abs(c4)**2
    




#plt.plot(t/Bz,p1,'r-','Linewidth',2)








    




