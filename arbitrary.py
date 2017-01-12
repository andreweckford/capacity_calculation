'''
Created on Jan 13, 2015

@author: andreweckford
'''

import numpy as np

#def set_parameters(bigDelta, t_on, t_off):
#    tauCO = 1
#    tauOD = 0.5
#    tauDC = 0.5
#    
#    lamb = np.array([0,1-np.exp(-1*bigDelta/tauCO)])
#    delta = 1 - np.exp(-1*bigDelta/tauOD)
#    chi = 1 - np.exp(-1*bigDelta/tauDC)
#    
#    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
#    
#    return [lamb,delta,chi,Px]
    
    
def genP(bigDelta, t_on, t_off):
    #lamb,delta,chi):
    sens = np.array([0.0,1.0])*bigDelta
    insens = np.array([0.5,0.5])*bigDelta
    reverse = np.array([0.0,0.0])*bigDelta
    nolink = np.array([0.0,0.0])*bigDelta

    r12 = insens
    r13 = nolink
    r21 = reverse
    r23 = insens
    r31 = sens
    r32 = reverse

    maps = [[[0],[1],[2]],[[0,2],[1]]]
    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
    P = []
    for i in range(0,len(sens)):
        P.append(np.array([[1-r12[i]-r13[i],r12[i],r13[i]],[r21[i],1-r21[i]-r23[i],r23[i]],[r31[i],r32[i],1-r31[i]-r32[i]]]))
        
    if any([np.any(t < 0) for t in P]) or any([np.any(t > 1) for t in P]):
        raise ValueError("Your parameters lead to an invalid transition probability matrix. Try decreasing time step.")

    return [P,Px,maps]
    
