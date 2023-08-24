from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes, isPrime
import math
from src.RSA import FERMAT
from src.RSA import WIENER


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
    if WIENER.wiener_attack(N,e):
        return
    print("Testing Fermat Factorization...")
    if FERMAT.fermat(N, e):
        return
    print()
    print("Your parameters were strong enough to pass CryptoResolve!\nBut always be careful when using RSA!")
    return




