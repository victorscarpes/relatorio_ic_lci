import numpy as np
from vspc_tools import * #pode ser encontrado em https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 15})
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 200

# Regulação de linha

data = np.loadtxt('data/mirror_data/mirror_out_vdd.csv', delimiter=',', skiprows=1)
Iout, Vdd = np.split(data, 2 , axis=1)
Iout = Iout.flatten()
Vdd = Vdd.flatten()

fig, ax = plt.subplots()
ax.plot(Iout, Vdd)
ax.set_xlabel('$V_{dd}$')
ax.set_ylabel('$I_{out}$')
ax.xaxis.set_ticks([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
ax.set_xlim([0, 1.8])
ax.xaxis.set_major_formatter(eng_formatter(unit='V', precision=1, format=False))
ax.yaxis.set_major_formatter(eng_formatter(unit='A', precision=2))
plt.grid()
plt.tight_layout()
plt.show()

# Regulação de linha (parametrização da tensão de saída)

data_0_7 = np.loadtxt('data/mirror_data/vout_par/iout-0_7.csv', delimiter=',', skiprows=1)
Iout_0_7, Vdd_0_7 = np.split(data_0_7, 2 , axis=1)
Iout_0_7 = Iout_0_7.flatten()
Vdd_0_7 = Vdd_0_7.flatten()

data_0_92 = np.loadtxt('data/mirror_data/vout_par/iout-0_92.csv', delimiter=',', skiprows=1)
Iout_0_92, Vdd_0_92 = np.split(data_0_92, 2 , axis=1)
Iout_0_02 = Iout_0_92.flatten()
Vdd_0_92 = Vdd_0_92.flatten()

data_1_14 = np.loadtxt('data/mirror_data/vout_par/iout-1_14.csv', delimiter=',', skiprows=1)
Iout_1_14, Vdd_1_14 = np.split(data_1_14, 2 , axis=1)
Iout_1_14 = Iout_1_14.flatten()
Vdd_1_14 = Vdd_1_14.flatten()

data_1_36 = np.loadtxt('data/mirror_data/vout_par/iout-1_36.csv', delimiter=',', skiprows=1)
Iout_1_36, Vdd_1_36 = np.split(data_1_36, 2 , axis=1)
Iout_1_36 = Iout_1_36.flatten()
Vdd_1_36 = Vdd_1_36.flatten()

data_1_58 = np.loadtxt('data/mirror_data/vout_par/iout-1_58.csv', delimiter=',', skiprows=1)
Iout_1_58, Vdd_1_58 = np.split(data_1_58, 2 , axis=1)
Iout_1_58 = Iout_1_58.flatten()
Vdd_1_58 = Vdd_1_58.flatten()

data_1_8 = np.loadtxt('data/mirror_data/vout_par/iout-1_8.csv', delimiter=',', skiprows=1)
Iout_1_8, Vdd_1_8 = np.split(data_1_8, 2 , axis=1)
Iout_1_8 = Iout_1_8.flatten()
Vdd_1_8 = Vdd_1_8.flatten()

fig, ax = plt.subplots()
ax.plot(Iout_0_7, Vdd_0_7, label='$V_{out}$ = 700 mV')
ax.plot(Iout_0_92, Vdd_0_92, label='$V_{out}$ = 920 mV')
ax.plot(Iout_1_14, Vdd_1_14, label='$V_{out}$ = 1,14 V')
ax.plot(Iout_1_36, Vdd_1_36, label='$V_{out}$ = 1,36 V')
ax.plot(Iout_1_58, Vdd_1_58, label='$V_{out}$ = 1,58 V')
ax.plot(Iout_1_8, Vdd_1_8, label='$V_{out}$ = 1,8 V')
ax.set_xlabel('$V_{dd}$')
ax.set_ylabel('$I_{out}$')
ax.xaxis.set_ticks([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
ax.set_xlim([0, 1.8])
ax.xaxis.set_major_formatter(eng_formatter(unit='V', precision=1, format=False))
ax.yaxis.set_major_formatter(eng_formatter(unit='A', precision=2))
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Regulação de linha (tensão de saída variando com a tensão de alimentação)

data = np.loadtxt('data/mirror_data/iout_vout_equal_vdd.csv', delimiter=',', skiprows=1)
Iout, Vdd = np.split(data, 2 , axis=1)
Iout = Iout.flatten()
Vdd = Vdd.flatten()

fig, ax = plt.subplots()
ax.plot(Iout, Vdd)
ax.set_xlabel('$V_{dd}$')
ax.set_ylabel('$I_{out}$')
ax.xaxis.set_ticks([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
ax.set_xlim([0, 1.8])
ax.xaxis.set_major_formatter(eng_formatter(unit='V', precision=1, format=False))
ax.yaxis.set_major_formatter(eng_formatter(unit='A', precision=2))
plt.grid()
plt.tight_layout()
plt.show()

# Sensibilidade térmica

data = np.loadtxt('data/mirror_data/mirror_out_temp.csv', delimiter=',', skiprows=1)
Iout, T = np.split(data, 2 , axis=1)
Iout = Iout.flatten()
T = T.flatten()
dI_dT = np.gradient(Iout, T)

fig, ax = plt.subplots()
ax.plot(Iout, T)
ax.set_xlabel('$T$')
ax.set_ylabel('$I_{out}$')
ax.xaxis.set_ticks([0, 20, 40, 60, 80, 100])
ax.xaxis.set_ticklabels(['0°C', '20°C', '40°C', '60°C', '80°C', '100°C'])
ax.set_xlim([0, 100])
ax.yaxis.set_major_formatter(eng_formatter(unit='A', precision=1))
plt.grid()
plt.tight_layout()
plt.show()