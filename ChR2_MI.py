import numpy as np
import channelrhodopsin as ch
import genMarkov as gm

def ChR2_MI(bigDelta,px0):

  Q = ch.genP(bigDelta, bigDelta/(1-px0), bigDelta/px0)

  P0 = Q[0][0]
  P1 = Q[0][1]
  Py = P0*px0 + P1*(1-px0)

  phiy = Py*np.log2(Py+(Py==0).astype(float))
  phi0 = P0*np.log2(P0+(P0==0).astype(float))
  phi1 = P1*np.log2(P1+(P1==0).astype(float))

  py_ss = gm.getSteadyStateDist(Py)

  foo = px0*phi0 + (1-px0)*phi1 - phiy

  result = sum(foo[0])*py_ss[0]*1000./bigDelta

  return result

