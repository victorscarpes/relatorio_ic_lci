import numpy as np
from vspc_tools import * #pode ser encontrado em https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 15})
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 200

# Regulação de linha

data = np.loadtxt('data/core_data/core_out_vdd.csv', delimiter=',', skiprows=1)
Iout, Vdd = np.split(data, 2 , axis=1)
Iout = Iout.flatten()
Vdd = Vdd.flatten()

fig, ax = plt.subplots()
ax.plot(Iout, Vdd)
ax.set_xlabel('$V_{dd}$')
ax.set_ylabel('$I_{X}$')
ax.xaxis.set_ticks([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
ax.set_xlim([0, 1.8])
ax.xaxis.set_major_formatter(eng_formatter(unit='V', precision=1, format=False))
ax.yaxis.set_major_formatter(eng_formatter(unit='A', precision=2))
plt.grid()
plt.tight_layout()
plt.show()

# Sensibilidade térmica

data = np.loadtxt('data/core_data/core_out_temp.csv', delimiter=',', skiprows=1)
Iout, T = np.split(data, 2 , axis=1)
Iout = Iout.flatten()
T = T.flatten()

fig, ax = plt.subplots()
ax.plot(Iout, T)
ax.set_xlabel('$T$')
ax.set_ylabel('$I_{X}$')
ax.xaxis.set_ticks([0, 20, 40, 60, 80, 100])
ax.xaxis.set_ticklabels(['0°C', '20°C', '40°C', '60°C', '80°C', '100°C'])
ax.set_xlim([0, 100])
ax.yaxis.set_major_formatter(eng_formatter(unit='A', precision=2))
plt.grid()
plt.tight_layout()
plt.show()