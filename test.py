import time
import numpy as np
from math import log,floor
from scipy.stats import norm
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

#Tool functions for FHE
from utils import draw_from_binary,draw_from_integer,draw_from_normal
from utils import mod, base_decomp, base_decomp_vec, draw_from_integer_vec

from fhe import LWE, inv_LWE
from fhe import RLWE,inv_RLWE,RLWE_prod
from fhe import RGSW,prod_ext

from utils import draw_from_binary_vec
from bootstrap import get_BK, accu_AP, extract_RLWE, key_switch
from bootstrap import get_BK_dec, accu_AP_dec
# security parameters
N = int(2**9)
q = int(2**6)
B = int(2**1)

sigma = 0.1
t = 2

s_ini = draw_from_binary(n=N)
s_new = draw_from_binary(n=N)

# draw message
m0 = draw_from_binary(n=int(2**3))


# code with secret key s
a_in,b_in = RLWE(n=N,q=q,sigma=sigma,s=s_ini,t=t,m=m0)
# Perform keyswitch
a_new, b_new = key_switch(n=N, q=q, B=B,sigma=0.1, t=t,s=s_new, s_prime=s_ini, a_prime=a_in, b_prime=b_in)
# decode
m_decoded = inv_RLWE(n=int(2**3), q=q, s=s_new, t=t, a=a_new, b=b_new)
print("m0=",m0.coef)
print("m_decoded=",m_decoded.coef)
