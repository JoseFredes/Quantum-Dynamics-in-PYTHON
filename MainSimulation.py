import math
import numpy as np
from getSci import getSci
import matplotlib.pyplot as plt
import scipy.linalg as scl;
#variables
Nspins = 2
j = 13
Bz = 5
hbar = 1

#matrices
Sx = np.matrix([[0,1],[1,0]])
Sz = np.matrix([[1,0],[0,-1]])
I = np.matrix([[1,0],[0,1]])

#hamiltonianio
H = -j * np.kron(Sx,Sx) - Bz * (np.kron(Sz,I)+np.kron(I,Sz))

#condicion inicial
RightState = np.matrix([[1],[1]])/math.sqrt(2)
Psi_0 = np.kron(RightState,RightState)


#tiempo
ti = 0
tf = 15/Bz
N = 1000
dt =(tf-ti)/(N)
t = np.arange(ti,tf,dt)


#dinamica 
psi = Psi_0

#magnetizacion
Mx = 0
Mz = 0

for i in range(1,Nspins+1):
    Sxi = getSci(Sx,i,Nspins)
    Szi = getSci(Sz,i,Nspins)
    Mx = Mx + Sxi/Nspins
    Mz = Mz + Szi/Nspins

print(Mx)
print(Mz)

#funciones
c1 = np.zeros([1,N], dtype=np.complex_)
c2 = np.zeros([1,N], dtype=np.complex_)
c3 = np.zeros([1,N], dtype=np.complex_)
c4 = np.zeros([1,N], dtype=np.complex_)
PromMx = np.zeros([1,N], dtype=np.complex_)
PromMZ = np.zeros([1,N], dtype=np.complex_)

# Operador evolucion temporal
U = scl.expm(-1j*H/hbar*dt)
print(U)

for n in range(0,N):
    if n == 0:
        psi = Psi_0
        c1[0][n] = psi[0]
        c2[0][n] = psi[1]
        c3[0][n] = psi[2]
        c4[0][n] = psi[3]
        PromMx[0][n] = psi.getH() * Mx * psi
        PromMZ[0][n] = psi.getH() * Mz * psi
    else:
        psi =  U*psi

        c1[0][n] = psi[0]
        c2[0][n] = psi[1]
        c3[0][n] = psi[2]
        c4[0][n] = psi[3]
        PromMx[0][n] = psi.getH() * Mx * psi 
        PromMZ[0][n] = psi.getH() * Mz * psi

        #probabilidades
        p1 = abs(c1)**2
        p2 = abs(c2)**2
        p3 = abs(c3)**2
        p4 = abs(c4)**2
    

P1 = p1[0][:]
P2 = p2[0][:]
P3 = p3[0][:]
P4 = p4[0][:]
MeanMz = PromMZ[0][:]
MeanMx = PromMx[0][:]


lineW = 2 # Line thickness
plt.figure(figsize=(10,8))
# plt.subplot(2,2,1)
plt.plot(t, P1,'--r', label='P_1'); 
plt.plot(t, P2,'--g', label='P_2'); 
plt.plot(t, P3,'--b', label='P_3'); 
plt.plot(t, P4,'--k', label='P_4'); 
plt.ylabel('M_x');plt.xlabel('t')
plt.legend()


lineW = 2 # Line thickness
plt.figure(figsize=(10,8))
# plt.subplot(2,2,1)
plt.plot(t, MeanMz,'--r', label='<M_z>'); 
plt.ylabel('M_z');plt.xlabel('t')
plt.legend()

lineW = 2 # Line thickness
plt.figure(figsize=(10,8))
# plt.subplot(2,2,1)
plt.plot(t, MeanMx,'--b', label='<M_x>'); 
plt.ylabel('M_x');plt.xlabel('t')
plt.legend()