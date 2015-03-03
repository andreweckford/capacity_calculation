'''
Created on Mar 3, 2015

@author: andreweckford
'''

import numpy as np

def genP(bigDelta, t_on, t_off):
    
    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
    
    maps = [[[0],[1],[2],[3],[4],[5],[6],[7],[8]],[[0,1,2,3],[4,5,6,7,8]]]
    
    x_array = np.array([1e-7,5e-4])
    
    # units are per second -- multiply by 1e-3 later to make them per ms
    kPlus1N = 7.7e8 # per mol
    kPlus2N = 3.2e10 # per mol
    kMinus1N = 1.6e5
    kMinus2N = 2.2e4
    kPlus1C = 8.4e7 # per mol
    kPlus2C = 3.3e7 # per mol
    kMinus1C = 8.7e3
    kMinus2C = 9.8
    
    P = []
    
    for x in x_array:
        RN = np.array([[0,kPlus1N*x,0],[kMinus1N,0,kPlus2N*x],[0,kMinus2N,0]])
        dPlus1 = np.identity(3)*kPlus1C*x
        dPlus2 = np.identity(3)*kPlus2C*x
        dMinus1 = np.identity(3)*kMinus1C
        dMinus2 = np.identity(3)*kMinus2C
        z = np.zeros((3,3))
        
        R = np.hstack((RN,dPlus1,z)) # first row
        R = np.vstack((R,np.hstack((dMinus1,RN,dPlus2))))
        R = np.vstack((R,np.hstack((z,dMinus2,RN))))
        
        # make diagonal equal to zero
        R = R - np.diag(np.sum(R,axis=1))
        
        # scale per ms rather than per s
        R = R * (1e-3)
        
        # append to P
        P.append(np.identity(9)+bigDelta*R)
        
    return [P,Px,maps]
    
    

