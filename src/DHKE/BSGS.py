import math
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long


# Baby Step Giant Step algorithm to solve the DLP on small values


def BSGS(g, N, B):
    m = math.ceil(math.sqrt(N))
    table = []
    for j in range(m):
        table.append(j, (pow(g, j, N)))
    inv = pow(g, -m, N)
    y = B
    for i in range(m):
        if y == table[i][1]:
            return i*m + table[i][0]
        else:
            y = y * inv



