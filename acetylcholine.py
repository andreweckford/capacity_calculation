'''
Created on Feb 5, 2015

@author: andreweckford
'''

import numpy as np

def genP(bigDelta, t_on, t_off):
    
    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
    
    # State numbering: (labels from Colquhoun and Hawkes, 1982)
    # 0 = AR
    # 1 = A2R
    # 2 = A2T
    # 3 = AT
    # 4 = T
    
    maps = [[[0],[1],[2],[3],[4]],[[0,1],[2,3,4]]]

    # parameter values taken from Colquhoun and Hawkes, 1982
    # rates at the reference are in seconds, these are in ms
    kPlus1 = 50000 # per mol
    kMinus1 = 2 # insensitive to concentration
    kPlus2 = 500000 # per mol
    kMinus2 = 2 # insensitive to concentration
    beta1 = 0.015 # insensitive
    alpha1 = 3 # insensitive
    beta2 = 15 # insensitive
    alpha2 = 0.5 # insensitive
    kStarPlus2 = kPlus1 # per mol
    kStarMinus2 = 0.00033 # per mol
    
    xA_array = np.array([1e-7,1e-5])
    
    P = []
    
    for xA in xA_array:
        # in R, rows sum to 0
        R = np.array([
                      [-1*(alpha1+kStarPlus2*xA),kStarPlus2*xA,0,alpha1,0],
                      [2*kStarMinus2,-1*(alpha2 + 2*kStarMinus2),alpha2,0,0],
                      [0,beta2,-1*(beta2+2*kMinus2),2*kMinus2,0],
                      [beta1,0,kPlus2*xA,-1*(beta1+kPlus2*xA+kMinus1),kMinus1],
                      [0,0,0,2*kPlus1*xA,-2*kPlus1*xA]
                      ])
        #print(R)
        P.append(np.identity(5) + bigDelta*R)

    if any([np.any(t < 0) for t in P]) or any([np.any(t > 1) for t in P]):
        raise ValueError("Your parameters lead to an invalid transition probability matrix. Try decreasing time step.")

    
    #print(P)
    return [P,Px,maps]

