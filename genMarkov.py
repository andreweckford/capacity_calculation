'''
Created on Jan 5, 2015

@author: andreweckford

These routines generate both stationary and non-stationary Markov processes, and provide some additional tools.
- randNonUniform: generates non-uniformly-distributed discrete random variables.
- generateMarkov: generates a stationary Markov process
- generateNonStationaryMarkov: generates a non-stationary Markov process, where a vector x chooses the state transition probability matrix to use
- getSteadyStateDist: gets the steady-state distribution of a Markov transition probability matrix
- getNonStationarySteadyStateDist: gets the steady-state distribution of a non-stationary Markov process (as in generateNonStationaryMarkov), where x is either iid or Markov
- findInArray: finds an element in a numpy array, within a given tolerance
'''

import numpy as np

def randNonUniform(p,n=1):
    """
    Generates a 1-by-n array with random variables according to the distribution in p.
    Generates 0 w.p. p[0], 1 w.p. p[1], etc.; p must sum to 1.
    If n is not given, a scalar is returned.
    """
    cdf = np.cumsum(p)
    r = np.random.rand(n)
    result = np.array([0]*n)
    for i in range(0,n):
        for j in cdf:
            if (r[i] > j):
                result[i] += 1
    return result

def generateMarkov(P,n,initd=None):
    """
    Generates a 1-by-n array with random variables according to the state transition matrix P.
    P is a numpy array.
    initd is an array containing the initial distribution. If none is provided, the steady-state distribution is used.
    """
    if initd==None:
        # replace with steady-state distribution
        initd = getSteadyStateDist(P)
    result = np.array([0]*n)
    result[0] = randNonUniform(initd)
    for i in range(1,n):
        result[i] = randNonUniform(P[result[i-1],:])
    return result

def generateNonStationaryMarkov(P,x,n,initd):
    """
    P is a list of Markov transition probability matrices, each one is a numpy array, each one row-stochastic
    x is a discrete vector where x[i] in 0,1,...,k; where k = len(P)-1
    n is the length of the output
    initd is the initial distribution over the output conditioned on x - a k-by-(dimension of P[i]) matrix (MUST be supplied)
    out[i+1] is selected from out[i] and P[x[i+1]]
    """
    result = np.array([0]*n)
    result[0] = randNonUniform(initd[x[0],:])
    for i in range(1,n):
        result[i] = randNonUniform(P[x[i]][result[i-1],:])
    return result

def pxTransform(Px):
    """
    if Px starts out as a 1-by-k numpy array, returns a k-by-k array where all rows are the same
    (like the Markov "state transition matrix" of an iid process)
    if Px starts out as a matrix, it is returned, unchanged
    """
    k = Px.shape[0]
    if (len(Px.shape)==1):
        # turn this into a square matrix
        # every row the same
        Px = np.vstack((Px,)*k)
    return Px

def sizes(P,Px):
    """
    For a nonstationary markov chain,
    returns the tuple (nx,ny), where nx is the number of distinct x elements (# of columns in Px)
    and ny is the number of distinct y elements (# of rows/columns in any element of P)
    """
    nx = Px.shape[0]
    ny = P[0].shape[0]
    return (ny,nx)

def bigXYmatrix(P,Px):
    """
    Returns the matrix representing the joint process X and Y, as a numpy array.
    """
    (ny,nx) = sizes(P,Px)
    Px = pxTransform(Px)
    for i in range(0,nx):
        for j in range(0,nx):
            h = np.array(Px[i,j]*P[i]) # error correction? used to be P[j]
            if (j == 0):
                foo = h
            else:
                foo = np.hstack((foo,h))
        if (i == 0):
            result = foo
        else:
            result = np.vstack((result,foo))
    return result
    

def getNonStationarySteadyStateDist(P,Px):
    """
    Finds the steady state distribution for a given non-stationary Markov process
    where there are k possible Markov transition probability matrices, controlled by k 
    P is a list of k Markov transition probability matrices, each one is a numpy array, each one row-stochastic
    Px is either: a 1-by-k numpy array (x is iid) or a k-by-k numpy array (x is Markov with TP matrix Px)
    Returns a 3-tuple consisting of: marginal distribution of y; conditional distribution of y given x; joint distribution of x and y 
    """
    Px = pxTransform(Px)
    k = Px.shape[0]
    # assemble the X-Y matrix
    result = bigXYmatrix(P,Px)
    ssTemp = getSteadyStateDist(result)
    # ssTemp is a stationary distribution on (x,y)
    # extract the stationary distribution on y only
    a = P[0].shape[0]
    ss = np.zeros(a)
    for i in range(0,a):
        for j in range(0,k):
            ss[i] = ss[i] + ssTemp[i+j*a]
    
    sc = np.zeros((k,a)) # k rows, a columns
    # extract the conditional distribution of y given x   
    for i in range(0,a):
        for j in range(0,k):
            sc[j,i] = ssTemp[i+j*a]
    
    for j in range(0,k):
        sc[j,:] = sc[j,:]/sum(sc[j,:])
            
    return (np.array(ss),np.array(sc),ssTemp)
                
def getSteadyStateDist(P):
    """
    Finds the steady-state distribution for a given Markov matrix P. P is a numpy array and must be row-stochastic.
    """
    foo = np.linalg.eig(np.transpose(P))
    initd = np.abs(foo[1][:,findInArray(foo[0],1.0)]) #should be all positive and real -- eliminate vestigial imaginary components
    initd = initd / sum(initd)
    return initd

def findInArray(a,target,tol=1e-11):
    """
    Returns the index of the target in an array, with the given tolerance.
    Returns None if the element is not found.
    If there is more than one, returns the index of the first.
    """
    count=0;
    for i in a:
        if np.abs(i-target) < tol:
            return count
        count += 1
    return None

def generateNonStationaryHiddenMarkov(P,x,n,initd,mymap):
    """
    Generates a non-stationary hidden Markov process by "hiding" outputs according to the map.
    For example, if the output states are 0,1,2,3 and mymap=[[0,2],[1,3]], then outputs 0,2 map to 0 and 1,3 map to 1
    mymap must be a list of lists.
    """
    # invert the map
    invmap = np.zeros(P[0].shape[0])
    for i in range(0,len(invmap)):
        for j in range(0,len(mymap)):
            if i in mymap[j]:
                invmap[i] = j
                
    temp = generateNonStationaryMarkov(P,x,n,initd)
    for i in range(0,len(temp)):
        temp[i] = invmap[temp[i]]
    return temp