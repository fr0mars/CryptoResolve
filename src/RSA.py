from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes, isPrime
import math

def test_parameters():
    print()
    print("Getting your RSA parameters...")
    mod = input("What is your Modulus (decimal input) ?\nModulus:  ")
    try:
        modulus = int(mod)
    except ValueError:
        print("Error: Invalid Modulus Format")
        return
    exp = input("What is your public exponent (decimal input) ?\nExponent:  ")
    try:
        exponent = int(exp)
    except ValueError:
        print("Error: Invalid Exponent Format")
        return
    print()
    print("Public key successfully received!")
    print("Testing your parameters...\n")
    return check_params(modulus,exponent)


def check_params(N, e):
    print("Testing primality of the Modulus...")
    if isPrime(N):
        print()
        print(f"Your Modulus is a prime number which leads to an easy\ncomputation of the euler totient and your private key.")
        try:
            inv = inverse(e, N-1)
            print(f"Euler Totient = {N-1}\nPrivate key = {inv}")
        except ValueError:
            print("In fact, your exponent is not even invertible in the given Modulus\n")
        return
    print("Testing custom Wiener attack...")
    if wiener_attack(N,e):
        return
    print("Testing Fermat Factorization...")
    if fermat(N, e):
        return
    print()
    print("Your parameters were strong enough to pass CryptoResolve!\nBut always be careful when using RSA!")
    return


def wiener_attack(N,e):
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
        return True
    return False


def fermat(N, e):
    def is_perfect_square(n):
        """
         quick test to know if an integer n is a perfect square
        """
        endings = ["00", "21", "41", "64", "89", "01", "24", "44", "69", "96", "04", "25", "49", "76", "09", "29", "56",
                   "81", "16", "36", "61", "84"]
        if str(n)[-2:] in endings:
            return True
        return False

    def fermat_factorization(N):
        """
         N : an odd integer
         returns:  two integers c, d such as N = cd
        """
        a = math.isqrt(N)
        b_square = a * a - N
        while not is_perfect_square(b_square):
            a += 1
            b_square = a * a - N
        b = math.isqrt(b_square)
        return a + b, a - b

    p,q = fermat_factorization(N)
    if p*q == N:
        print()
        print("Fermat Factorization attack was successful because\nthe factors of your Modulus were too close from eachothers")
        phi = (p-1)*(q-1)
        try:
            d = inverse(e, phi)
            print(f"Euler totient = {phi}\nPrivate key = {d}\n")
        except ValueError:
            print(f"Euler totient = {phi}")
            print("Also found that your exponent was not invertible in the given modulus\n")
        return True
    return False

