from Crypto.Util.number import long_to_bytes


def wiener_attack(N,e, m):
    def cf_expansion(n, d):
        e = []

        q = n // d
        r = n % d
        e.append(q)

        while r != 0:
            n, d = d, r
            q = n // d
            r = n % d
            e.append(q)

        return e

    def convergents(e):
        n = []  # Nominators
        d = []  # Denominators

        for i in range(len(e)):
            if i == 0:
                ni = e[i]
                di = 1
            elif i == 1:
                ni = e[i] * e[i - 1] + 1
                di = e[i]
            else:  # i > 1
                ni = e[i] * n[i - 1] + n[i - 2]
                di = e[i] * d[i - 1] + d[i - 2]

            n.append(ni)
            d.append(di)
            yield (ni, di)

    convergents = convergents(cf_expansion(e, N))
    privatekey = 1
    for k, d in convergents:
        if 1200 == pow(1200, e * d, N):
            privatekey = d
            break
    if privatekey != 1:
        print()
        print(f"Wiener attack was successful because your private key is too small\nPrivate key = {privatekey}")
        plain = pow(m,privatekey, N)
        print(f"decrypted message in decimal output= {plain}")
        print(f"decrypted message in bytes output= {long_to_bytes(plain)}")
        return True
    return False

