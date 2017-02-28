import numpy as np
import channelrhodopsin as ch
import genMarkov as gm

# partial entropy function
def pe(x):

  if (x == 0):
    return 0

  return -1*x*np.log2(x)

def ChR2_MI(bigDelta,px0):

  if bigDelta > 0:

    Q = ch.genP(bigDelta, bigDelta/(1-px0), bigDelta/px0)

    P0 = Q[0][0]
    P1 = Q[0][1]
    Py = P0*px0 + P1*(1-px0)

    phiy = Py*np.log2(Py+(Py==0).astype(float))
    phi0 = P0*np.log2(P0+(P0==0).astype(float))
    phi1 = P1*np.log2(P1+(P1==0).astype(float))

    py_ss = gm.getSteadyStateDist(Py)

    foo = px0*phi0 + (1-px0)*phi1 - phiy

    result = 1000.*sum(foo[0])*py_ss[0]/bigDelta

  else:

    # if bigDelta = 0, we get the value as delta T -> 0

    [lamb,delta,chi,Px] = ch.set_parameters(1.,1.,1.)
    q12L = lamb[0]
    q12H = lamb[1]
    q23 = delta
    q31 = chi
    qbar = lamb[0]*px0 + lamb[1]*(1-px0)
    
    result = 1000.*(pe(qbar) - px0*pe(q12L) - (1-px0)*pe(q12H))/(1 + qbar/q23 + qbar / q31)    

  return result

