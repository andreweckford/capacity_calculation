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

    # Model parameters -- putting period after an integer, like 1., makes the value a floating point
    # States are labelled 0,1,2
    # State transition rate from a to b is given by: alpha_ab_0 + alpha_ab_1*x
    alpha_01_0 = 1.
    alpha_01_1 = 1. 
    alpha_12_0 = 1. 
    alpha_12_1 = 1. 
    alpha_21_0 = 1.
    alpha_21_1 = 1.
    alpha_10_0 = 1.
    alpha_10_1 = 1.

    # I assume the input is binary and affects x; put the values you want for x here
    x = np.array([0.,1.])

    # here state 2 is observed, states 0,1 are hidden (i.e. we can only observe transitions in and out of state 2)
    # to customize this, please ask
    maps = [[[0],[1],[2]],[[0,1],[2]]]

    # convert Poisson rates to transition probabilities
    r01 = bigDelta*(alpha_01_0 + alpha_01_1*x)
    r10 = bigDelta*(alpha_10_0 + alpha_10_1*x)
    r12 = bigDelta*(alpha_12_0 + alpha_12_1*x)
    r21 = bigDelta*(alpha_21_0 + alpha_21_1*x)

    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
    P = []
    for i in range(0,len(x)):
        P.append(np.array([[1-r01[i],r01[i],0.],[r10[i],1-r10[i]-r12[i],r12[i]],[0.,r21[i],1-r21[i]]]))
        
    if any([np.any(t < 0) for t in P]) or any([np.any(t > 1) for t in P]):
        raise ValueError("Your parameters lead to an invalid transition probability matrix. Try decreasing time step.")

    return [P,Px,maps]
    
