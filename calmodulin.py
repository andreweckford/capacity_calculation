'''
Created on Mar 3, 2015

@author: andreweckford
'''

def genP(bigDelta, t_on, t_off):
    
    Px = np.array([[1-bigDelta/t_off,bigDelta/t_off],[bigDelta/t_on,1-bigDelta/t_on]])
    
    maps = [[[0],[1],[2],[3],[4],[5],[6],[7],[8]],[[0,1,2,3],[4,5,6,7,8]]]
    
    x_array = np.array([1e-7,5e-4])
    
    kPlus1N = 7.7e8 # per mol
    kPlus2N = 3.2e10 # per mol
    kMinus1N = 1.6e5
    kMinus2N = 2.2e4
    kPlus1C = 8.4e7 # per mol
    kPlus2C = 3.3e7 # per mol
    kMinus1C = 8700
    kMinus2C = 9.8
    
    P = []
    
    for x in x_array:
        RC = np.array([-1*kPlus1C*x,kPlus1C*x,0],
                      [kMinus1C,-1*(kMinus1C+kPlus2C*x),kPlus2C*x],
                      [0,kMinus2C,-1*kMinus2C])
        RN = np.array([-1*kPlus1N*x,kPlus1N*x,0],
                      [kMinus1N,-1*(kMinus1N+kPlus2N*x),kPlus2N*x],
                      [0,kMinus2N,-1*kMinus2N])
        R = np.kron(RC,RN)
        P.append(np.identity(9)+bigDelta*R)
        
    return [P,Px,maps]
    
    

