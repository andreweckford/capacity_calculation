'''
Created on Jan 13, 2015

@author: andreweckford
'''

import numpy as np

def set_parameters(bigDelta, t_on, t_off):
    tauCO = 0.2
    tauOD = 20
    tauDC = 60
    
    lamb = np.array([0,1-np.exp(-1*bigDelta/tauCO)])
    delta = 1 - np.exp(-1*bigDelta/tauOD)
    chi = 1 - np.exp(-1*bigDelta/tauDC)
    
    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
    
    return [lamb,delta,chi,Px]
    
    
def genP(bigDelta, t_on, t_off):
    #lamb,delta,chi):
    maps = [[[0],[1],[2]],[[0,2],[1]]]
    [lamb,delta,chi,Px] = set_parameters(bigDelta, t_on, t_off)
    P = []
    for i in range(0,len(lamb)):
        P.append(np.array([[1-lamb[i],lamb[i],0],[0,1-delta,delta],[chi,0,1-chi]]))
        
    if any([np.any(t < 0) for t in P]) or any([np.any(t > 1) for t in P]):
        raise ValueError("Your parameters lead to an invalid transition probability matrix. Try decreasing time step.")

    return [P,Px,maps]
    
