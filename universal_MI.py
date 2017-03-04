import numpy as np
import channelrhodopsin as ch
import genMarkov as gm

# P is the list of arrays returned by genP for the appropriate receptor
# px is a vector of the same length as P, containing the iid probabilities of the inputs
# bigDelta is the size of the time step (for calculating the information rate as a function of time)
def universal_MI(P,px,bigDelta):

  Py = P[0] * px[0]
  for i in range(1,len(px)):
    Py = Py + P[i]*px[i]

  phiy = Py*np.log2(Py+(Py==0).astype(float))
  phix_m = [P[i]*np.log2(P[i]+(P[i]==0).astype(float)) for i in range(0,len(P))]

  phix = phix_m[0] * px[0]
  for i in range(1,len(px)):
    phix = phix + phix_m[i] * px[i]

  qq = phix - phiy

  pyy = gm.getSteadyStateDist(Py)

  return np.sum([pyy[i]*np.sum(qq[i,:]) for i in range(0,len(pyy))])*1000/bigDelta



