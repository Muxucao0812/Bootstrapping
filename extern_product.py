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
N = int(2**7)
q = int(2**50)
B = int(2**1)

print('k=',floor(log(q,B)))
sigma = 0.2
t = 2**25
s = draw_from_binary(n=N)
right = 0
false = 0
for _ in range(100):
    m0 = draw_from_binary(n=N//2-1)

    m1 = draw_from_binary(n=N//2-1)


    # compute prod for clear messages
    m0m1 = mod(poly=m0*m1,q=q,poly_modulus=np.poly1d([1] + ((N - 1) * [0]) + [1]))


    # encode product
    a_cifer,b_cifer = RLWE_prod(n=N,q=q,sigma=sigma,s=s,t=t,B=B,m0=m0,m1=m1)
    # decode product
    m0m1_decoded = inv_RLWE(n=N, q=q, s=s, t=t, a=a_cifer, b=b_cifer)
    if m0m1==m0m1_decoded:
        right+=1
    else:
        false+=1
print('right number:',right, 'false number:',false)