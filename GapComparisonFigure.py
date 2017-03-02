import numpy as np
from parse_result import *
from ChR2_MI import ChR2_MI
import matplotlib.pyplot as plt

q = parse_result('result.csv')
q02 = q[0::2]
q10 = q[1::2]

x = np.arange(0.94,0.9999,0.001)
y02 = [ChR2_MI(0.02,i) for i in x]
y10 = [ChR2_MI(0.1,i) for i in x]

plt.plot(x,y10,'g-',label='$\mathcal{I}(X;Y)$, $\Delta t = 0.1$ ms')
plt.plot(q10[:,4],q10[:,5],'go',label='$\mathcal{I}(X;Z)$, $\Delta t = 0.1$ ms')
plt.plot(x,y02,'b-',label='$\mathcal{I}(X;Y)$, $\Delta t = 0.02$ ms')
plt.plot(q02[:,4],q02[:,5],'bo',label='$\mathcal{I}(X;Z)$, $\Delta t = 0.02$ ms')
plt.axis([0.94,1,45,75])
plt.xlabel('Probablility of low light intensity $p_{\mathsf{L}}$')
plt.ylabel('Mutual information (bits/s)')
plt.grid()
plt.legend(loc='upper left')


plt.savefig('GapComparisonFigure.pdf')
plt.show()

