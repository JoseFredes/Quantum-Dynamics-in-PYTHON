import numpy as np

#getsci

def getSci(sc,i,Nspins):
    Is = np.eye(2)
    Op_total = np.array([1,Nspins],dtype= object)
    
    for site in (1,Nspins):
        Op_total[site] = Is + np.double(np.equal( i,site)) * (sc - Is)

    Sci = Op_total[1]
    for site  in range(2,Nspins):
        Sci = np.kron(Sci,Op_total[site])

    return Sci

   