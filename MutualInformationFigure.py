import numpy as np
import matplotlib.pyplot as plt
from ChR2_MI import ChR2_MI

# Generates figure tagged fig:MutualInformationFigure in the paper

x = np.arange(0.001,0.2,0.001)
plt.clf()
plt.xlabel('Off probability')
q = [[ChR2_MI(j,1-i) for i in x] for j in [0.01]+list(np.arange(0.02,0.12,0.02))]
for c in range(0,len(q)):
  plt.plot(x,q[c])

qq = [ChR2_MI(0,1-i) for i in x]
plt.plot(x,qq,'k--')

plt.axis([0.,0.2,20.,80.])
plt.xlabel('Illumination probability')
plt.ylabel('Mutual information (bits/s)')
plt.grid()
plt.savefig('MutualInformationFigure.pdf')
plt.show()

