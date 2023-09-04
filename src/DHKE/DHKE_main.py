import math

from Crypto.Util.number import isPrime
from DHKE.BSGS import BSGS
# This Section mostly relies on solving the DLP by Pohlig-Hellman or BSGS on small DH keys




# determine if g is a primitive root of the multiplicative group of modulus N
# Modulus is assumed to be a prime here


def get_divisors(n):
    for i in range(1, n):
        if n%i ==0:
            yield i
    yield n



def is_primitive_root(g, N):
    phi = N-1
    divs = list(get_divisors(phi))
    n = len(divs)
    for i in range(n):
        if pow(g, divs[i], N) == 1:
            if divs[i] == phi:
                return True
            else:
                return False
    return False



def parameters():
    print()
    print("Getting Your Diffie-Hellman parameters...")
    mod = input("What is the Modulus of your multiplicative group (decimal input) ?\nModulus: ")
    try:
        modulus = int(mod)
    except ValueError:
        print("Error: Invalid Modulus Format")
        return
    gen = input("What is the primitive element of your multiplicative group (decimal input) ?\nElement: ")
    try:
        elt= int(gen)
    except ValueError:
        print("Error: Invalid Primitive element Format")
        return
    if not is_primitive_root(elt, modulus):
        print("Error: The given element is not a primitive root of your modulus")
        return
    public = input("What is your Public Key : primitive element ^ private key (decimal input) ?\n Public Key: ")
    try:
        PK= int(public)
    except ValueError:
        print("Error: Invalid Public Key Format")
        return
    print()
    print("Parameters successfully received!")
    print("Testing your parameters...\n")

    return check_params(modulus, elt, PK)


def check_params(N,g,B):
    if isPrime(N):
        print("Prime Modulus, trying BSGS algorithm...")
        exp = BSGS(g,B,N)
        print(f"Private key = {exp}")
        return
    else:
        return
