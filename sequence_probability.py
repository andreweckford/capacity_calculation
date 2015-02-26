'''
Created on Jan 7, 2015

@author: andreweckford
'''

# recovery method

import numpy as np
import genMarkov

def binent(p):
    """
    The binary entropy function of p.
    """
    return -1.0*p*np.log2(p) - (1.0-p)*np.log2(1.0-p)

def log2MarkovProbability(P,y,initd=None):
    """
    Calculates the log (base 2) of the probability of the Markov sequence y.
    y is a numpy array.
    P is the transition probability matrix.
    The optional parameter initd is the initial probability distribution; if none is supplied,
    the steady state distribution is used.
    """
    if (initd == None):
        result = np.log2(genMarkov.getSteadyStateDist(P)[y[0]])
    else:
        result = np.log2(initd)[y[0]]

    for i in range(1,len(y)):
        result = result + np.log2(P[y[i-1],y[i]])
        
    return result

def log2NonStationaryConditionalProbability(P,y,x,initd,mymap=None):
    """
    Calculates the log (base 2) of the probability of the Markov sequence y.
    y is a numpy array.
    P is a list of Markov transition probability matrices, each one is a numpy array, each one row-stochastic
    x is a discrete vector where x[i] in 0,1,...,k; where k = len(P)-1
    n is the length of the output
    initd is the initial distribution over the output conditioned on x - a k-by-(dimension of P[i]) matrix (MUST be supplied)
    mymap (optional) is a list OF LISTS which has the same dimension as the number of distinct outputs, and
    indicates which channel state map to which outputs. For example, suppose there are 3 distinct outputs and 4 channel states.
    Then mymap = [[0,2],[1],[3]] indicates that (0,2) map to y=0; 1 maps to y=1; and 3 maps to y=2.
    If mymap is not provided it is assumed that states and outputs are a bijection.
    out[i+1] is selected from out[i] and P[x[i+1]]
    """
    ns = P[0].shape[0]
    if (mymap == None):
        mymap = []
        for i in range(0,ns):
            mymap.append([i])
    
    # for now we will assume mymap is None
    
    message = initd[x[0],:]
    masks = np.zeros((len(mymap),ns))
    for i in range(0,len(mymap)):
        for j in range(0,len(mymap[i])):
            masks[i,mymap[i][j]] = 1
    
    message = message * masks[y[0],:]
    msg_norm = sum(message) # normalize the message and add (log 2) to the result
    message = message / msg_norm
    result = np.log2(msg_norm)
    for i in range(1,len(y)):
        foo = np.array(np.matrix(message)*np.matrix(P[x[i]]))
        message = foo[0] # for some reason this is necessary when matrices are transformed to arrays
        message = message * masks[y[i],:]
        msg_norm = sum(message) # normalize the message and add (log 2) to the result
        message = message / msg_norm
        result += np.log2(msg_norm)
    return result

#     result = np.log2(initd[x[0],y[0]])
#     for i in range(1,len(y)):
#         foo = P[x[i]] # foo is a numpy array
#         result = result + np.log2(foo[y[i-1],y[i]])
#         

def log2NonStationaryOutputProbability(P,y,Px,mymap=None,initd=None):
    """
    Calculates the log (base 2) of the 
    initd, if provided, is of the form provided by genMarkov.getNonStationarySteadyStateDist() 
    """
    Px = genMarkov.pxTransform(Px)
    (ny,nx) = genMarkov.sizes(P,Px)
    if (mymap == None):
        mymap = []
        for i in range(0,ny):
            mymap.append([i])
    if (initd == None):
        initd = genMarkov.getNonStationarySteadyStateDist(P, Px)
        
    xyMatrix = genMarkov.bigXYmatrix(P, Px)
    mask = np.zeros((len(mymap),ny*nx))
    for j in range(0,len(mymap)):
        for h in range(0,len(mymap[j])):
            for i in range(0,nx):
                mask[j,mymap[j][h]+ny*i] = 1
    
    # sum-product algorithm section
    message = initd[2]
    message = message * mask[y[0]]
    msg_norm = sum(message) # normalize the message and add (log 2) to the result
    message = message / msg_norm
    result = np.log2(msg_norm)
        
    for j in range(1,len(y)):
        foo = np.array(np.matrix(message)*np.matrix(xyMatrix))
        message = foo[0] # for some reason this is necessary when matrices are transformed to arrays
        message = message * mask[y[j]]
        msg_norm = sum(message)
        message = message / msg_norm
        result += np.log2(msg_norm)
        
    return result
        
def markovEntropy(P):
    """
    Returns the steady state entropy of the Markov chain with transition probability matrix P, in bits.
    """
    initd = genMarkov.getSteadyStateDist(P)
    initd = np.transpose(np.vstack((initd,)*(P.shape[0])))
    return -1*sum(sum(initd*P*np.log2(P)))
    
    
    
    