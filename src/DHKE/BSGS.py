import math



# Baby Step Giant Step algorithm to solve the DLP on small values


def BSGS(g, B, N):

    m = math.ceil(math.sqrt(N - 1))
    table = {pow(g, i, N): i for i in range(m)}
    c = pow(g, m * (N - 2), N)
    for j in range(m):
        y = (B * pow(c, j, N)) % N
        if y in table:
            return j * m + table[y]

