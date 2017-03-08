import numpy as np
import acetylcholine as ac
import matplotlib.pyplot as plt
from universal_MI import universal_MI
from parse_result import parse_result

q = parse_result('result-ACh.csv')

x = np.arange(0.65,1,0.001)
[P,px,maps] = ac.genP(0.02,1,1)
y = [universal_MI(P,[i,1-i],0.02) for i in x]

plt.clf()
plt.plot(x,y,'b-',label='$\mathcal{I}(X;Y)$')
plt.plot(q[:,4],q[:,5],'bo',label='$\mathcal{I}(X;Z)$')
plt.axis([0.65,1.,0.,400.])
plt.xlabel('Probablility of low light intensity $p_{\mathsf{L}}$')
plt.ylabel('Mutual information (bits/s)')
plt.grid()
plt.legend(loc='upper left')

plt.savefig('AChFigure.pdf')
plt.show()

