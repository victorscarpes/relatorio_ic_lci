import numpy as np
from vspc_tools import * #pode ser encontrado em https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 15})
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 200

I_SH = eng_inv('150 nA')
α_12 = 2
S_2 = 0.01
φt = eng_inv('25,8519915 mV')

Ix = np.linspace(1e-12, 1e-9, 1000)

def F(i):
    return np.sqrt(1+i)-2+np.log(np.sqrt(1+i)-1)

def V_x12(Ix):
    return φt*(F((α_12*Ix)/(I_SH*S_2))-F(Ix/(I_SH*S_2)))

fig, ax = plt.subplots()
ax.plot(Ix, V_x12(Ix), 'r')
ax.set_xlabel('$I_X$')
ax.set_ylabel('$V_X$')
ax.set_xscale('log')
ax.xaxis.set_ticks([1e-12, 1e-11, 1e-10, 1e-9])
ax.set_xticklabels(['1 pA', '10 pA', '100 pA', '1 nA'])
ax.yaxis.set_major_formatter(eng_formatter(unit='V', precision=2))
plt.grid()
plt.tight_layout()
plt.show()