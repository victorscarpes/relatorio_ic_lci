import numpy as np
from vspc_tools import * #pode ser encontrado em https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
from sbcs_designer import S_1, S_2, S_3, S_4, α_12, α_34, φt, I_SH
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 15})
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 200

data_x = np.loadtxt('data/scm_data/Vx_vs_Ix.csv', delimiter=',', skiprows=1)
Ix, Vx12 = np.split(data_x, 2 , axis=1)
Ix = Ix.flatten()
Vx12 = Vx12.flatten()

data_y = np.loadtxt('data/scm_data/Vy_vs_Ix.csv', delimiter=',', skiprows=1)
Iy, Vx34 = np.split(data_y, 2 , axis=1)
Iy = Iy.flatten()
Vx34 = Vx34.flatten()

def F(i):
    return np.sqrt(1+i)-2+np.log(np.sqrt(1+i)-1)

def V_x12(Ix):
    return φt*(F((α_12*Ix)/(I_SH*S_2))-F(Ix/(I_SH*S_2)))

def V_x34(Ix):
    return φt*(F((α_34*Ix)/(I_SH*S_4))-F(Ix/(I_SH*S_4)))

Ix_index_teorico = np.absolute(V_x34(Ix)-V_x12(Ix)).argmin()
Ix_op_teorico = Ix[Ix_index_teorico]
Vx_op_teorico = (V_x12(Ix_op_teorico)+V_x34(Ix_op_teorico))/2

Ix_index_simulado = np.absolute(Vx34-Vx12).argmin()
Ix_op_simulado = Ix[Ix_index_simulado]
Vx_op_simulado = (Vx12[Ix_index_simulado]+Vx12[Ix_index_simulado])/2

print('Ponto de operação Teórico:')
print('Ix = '+eng_notation(Ix_op_teorico, 'A', 6))
print('Vx = '+eng_notation(Vx_op_teorico, 'V', 6))
print('\nPonto de operação Simulado:')
print('Ix = '+eng_notation(Ix_op_simulado, 'A', 6))
print('Vx = '+eng_notation(Vx_op_simulado, 'V', 6))

fig, ax = plt.subplots()
ax.plot(Ix, V_x12(Ix), 'r', label='$SCM_{12}$', zorder=10)
ax.plot(Ix, V_x34(Ix), 'b', label='$SCM_{34}$', zorder=20)
ax.scatter([Ix_op_teorico], [Vx_op_teorico], color='k', marker='o', zorder=30)
ax.set_xlabel('$I_X$')
ax.set_ylabel('$V_X$')
ax.legend(loc='best')
ax.set_xscale('log')
ax.xaxis.set_ticks([1e-11, 2e-11, 5e-11, 1e-10])
ax.set_xticklabels(['10 pA', '20 pA', '50 pA', '100 pA'])
ax.yaxis.set_major_formatter(eng_formatter(unit='V', precision=1))
plt.grid()
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
ax.plot(Ix, Vx12, 'r', label='$SCM_{12}$', zorder=10)
ax.plot(Ix, Vx34, 'b', label='$SCM_{34}$', zorder=20)
ax.scatter([Ix_op_simulado], [Vx_op_simulado], color='k', marker='o', zorder=30)
ax.set_xlabel('$I_X$')
ax.set_ylabel('$V_X$')
ax.legend(loc='best')
ax.set_xscale('log')
ax.xaxis.set_ticks([1e-11, 2e-11, 5e-11, 1e-10])
ax.set_xticklabels(['10 pA', '20 pA', '50 pA', '100 pA'])
ax.yaxis.set_major_formatter(eng_formatter(unit='V', precision=1))
plt.grid()
plt.tight_layout()
plt.show()