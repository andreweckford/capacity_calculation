'''
Created on Jan 13, 2015

@author: andreweckford
'''

import numpy as np

# data from Winter et al., Biophysical J., May 1994
# here the rates are in ms^-1
#
def set_parameters(bigDelta, t_on, t_off):
    alpha1 = 0.1002
    beta1 = np.array([0.,0.00602]) # sensitive
    alpha2 = 0.0415
    beta2 = 0.2196
    
    #lamb = np.array([0,1-np.exp(-1*bigDelta/tauCO)])
    #delta = 1 - np.exp(-1*bigDelta/tauOD)
    #chi = 1 - np.exp(-1*bigDelta/tauDC)
    
    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
    
    return [alpha1,beta1,alpha2,beta2,Px]
    
    
def genP(bigDelta, t_on, t_off):
    #lamb,delta,chi):
    maps = [[[0],[1],[2]],[[0,1],[2]]]
    [a1,b1,a2,b2,Px] = set_parameters(bigDelta, t_on, t_off)
    P = []
    bD = bigDelta # for compactness
    for i in range(0,len(b1)):
        P.append(np.array([[1.-b1[i]*bD,b1[i]*bD,0.],[a1*bD,1.-(a1+b2)*bD,b2*bD],[0.,a2*bD,1-a2*bD]]))
        
    if any([np.any(t < 0) for t in P]) or any([np.any(t > 1) for t in P]):
        raise ValueError("Your parameters lead to an invalid transition probability matrix. Try decreasing time step.")

    return [P,Px,maps]
    
