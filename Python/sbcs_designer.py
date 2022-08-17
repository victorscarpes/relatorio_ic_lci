from scipy.optimize import fsolve
import numpy as np
from vspc_tools import * #pode ser encontrado em https://github.com/victorscarpes/vspc_tools

def extractor(file):
    data = np.loadtxt(file, delimiter=',', skiprows=1)
    VG, ID = np.split(data, 2 , axis=1)
    VG = VG.flatten()
    ID = ID.flatten()

    ln_ID = np.log(ID)
    gm_ID = np.gradient(ln_ID, VG)
    gm_ID_max = np.max(gm_ID)
    Vt0_index = np.absolute(gm_ID - 0.531*gm_ID_max).argmin()
    Vt0 = VG[Vt0_index]
    Is = 1.13636*ID[Vt0_index]

    return (Is, Vt0)

def associator(S, W, L):
    γ = S*L/W
    if γ > 1:
        Np, Ns = round(γ), 1
    else:
        Np, Ns = 1, round(1/γ)
    return Np, Ns

φt = eng_inv('25,8519915 mV')
I_out = eng_inv('20 pA')
i_f2 = 10
i_f4 = 0.01
α_12 = 2

W = eng_inv('220 nm')
L = eng_inv('19,995 um')

I_S, Vt0 = extractor('data/ish_extraction/IDxVG.csv')
I_SH = I_S*L/W

def F(i):
    return np.sqrt(1+i)-2+np.log(np.sqrt(1+i)-1)

S_2 = (I_out)/(I_SH*i_f2)
S_1 = (S_2*2)/(α_12-1)

V_x = φt*(F(α_12*i_f2)-F(i_f2))

def func(α):
    return F(α*i_f4) - F(i_f4) - V_x/φt

α_34 = fsolve(func, 10, maxfev=int(1e5))[0]

S_4 = (I_out)/(I_SH*i_f4)
S_3 = (S_4*2)/(α_34-1)

Np_1, Ns_1 = associator(S_1, W, L)
Np_2, Ns_2 = associator(S_2, W, L)
Np_3, Ns_3 = associator(S_3, W, L)
Np_4, Ns_4 = associator(S_4, W, L)
i_f3 = α_34*i_f4
i_f1 = α_12*i_f2

if __name__=="__main__":
    print(f"Erro: {sci_notation(abs(func(α_34)), '', 6)}\n")

    print(f"Vx = {eng_notation(V_x, 'V', 6)}")
    print(f"Vt₀ = {eng_notation(Vt0, 'V', 6)}\n")

    print(f"Iout = {eng_notation(I_out, 'A', 6)}")
    print(f"Ish = {eng_notation(I_SH, 'A', 6)}")
    print(f"Is = {eng_notation(I_S, 'A', 6)}\n")

    print(f"if₁ = {sci_notation(i_f1, '', 6)}")
    print(f"if₂ = {sci_notation(i_f2, '', 6)}")
    print(f"if₃ = {sci_notation(i_f3, '', 6)}")
    print(f"if₄ = {sci_notation(i_f4, '', 6)}\n")

    print(f"α₁₂ = {sci_notation(α_12, '', 6)}")
    print(f"α₃₄ = {sci_notation(α_34, '', 6)}\n")

    print(f"S₁ = {sci_notation(S_1, '', 6)}")
    print(f"S₂ = {sci_notation(S_2, '', 6)}")
    print(f"S₃ = {sci_notation(S_3, '', 6)}")
    print(f"S₄ = {sci_notation(S_4, '', 6)}\n")

    print(f"L = {eng_notation(L, 'm', 6)}")
    print(f"W = {eng_notation(W, 'm', 6)}\n")

    if Np_1 == 1:
        print(f"M1 - {Ns_1} em série")
    else:
        print(f"M1 - {Np_1} em paralelo")

    if Np_2 == 1:
        print(f"M2 - {Ns_2} em série")
    else:
        print(f"M2 - {Np_2} em paralelo")

    if Np_3 == 1:
        print(f"M3 - {Ns_3} em série")
    else:
        print(f"M3 - {Np_3} em paralelo")

    if Np_4 == 1:
        print(f"M4 - {Ns_4} em série")
    else:
        print(f"M4 - {Np_4} em paralelo")