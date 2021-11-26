import numpy as np

#getsci

def getSci(sc,i,Nspins):
    Is = np.matrix([[1,0],[0,1]])
    X = np.zeros((Nspins,2,2))
    
    for site in range(1,Nspins+1):
        X[site-1] = Is + np.double(np.equal(i,site))*(sc-Is)

#    print(X[0])
#    print(X[1])
    Y = X[0];
    for site  in range(1,Nspins):
        Y = np.kron(Y,X[site])
        
    Sci = Y
#    print(Sci)
    
    return Sci

for i in range(1,2):
    print(i)
