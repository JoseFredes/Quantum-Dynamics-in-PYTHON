import numpy as np

def getSci(sc,i,Nspins):
    Is = np.matrix([[1,0],[0,1]])
    X = np.zeros((Nspins,2,2))
    
    for site in range(1,Nspins+1):
        X[site-1] = Is + np.double(np.equal(i,site))*(sc-Is)

    Y = X[0];
    for site  in range(1,Nspins):
        Y = np.kron(Y,X[site])
        
    Sci = Y 
    return Sci


def getHamiltonian(j,Bz,Nspins,Sx,Sz):
    
   Hi = 0;
   for i in range(1,Nspins):
    Sxi_l = getSci(Sx,i,Nspins)
    Sxi_r = getSci(Sx,i+1,Nspins)
    Hi = Hi -j * np.dot(Sxi_l,Sxi_r )

    # Zeeman Hamiltonian
    Hz = 0;   
    for j in range(1,Nspins+1):
        Szi = getSci(Sz,j,Nspins)
        Hz = Hz - Bz * Szi  

    # Hamiltonian
    H = Hi + Hz
    return H

def getInitialState(Psi0,Nspins):
    
    Y = Psi0;
    for site  in range(1,Nspins):
        Y = np.kron(Y,Psi0)
        
    PSI = Y
    return PSI
    