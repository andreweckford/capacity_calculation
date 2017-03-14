import numpy as np
import calmodulin as cm
import matplotlib.pyplot as plt
from universal_MI import universal_MI
from parse_result import parse_result

q = parse_result('result-CaM.csv')

x = np.arange(0,1,0.001)
[P,px,maps] = cm.genP(0.002,1,1)
y = [universal_MI(P,[i,1-i],0.002) for i in x]

plt.clf()
plt.plot(x,y,'b-',label='$\mathcal{I}(X;Y)$')
plt.plot(q[:,4],q[:,5],'bo',label='$\mathcal{I}(X;Z)$')
plt.axis([0.3,0.7,0.,350.])
plt.xlabel('Probablility of low ligand concentration $p_{\mathsf{L}}$')
plt.ylabel('Mutual information (bits/s)')
plt.grid()
plt.legend(loc='upper left')

plt.savefig('CaMFigure.pdf')
plt.show()

