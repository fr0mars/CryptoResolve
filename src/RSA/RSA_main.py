from Crypto.Util.number import inverse, isPrime, bytes_to_long, long_to_bytes
import math
from RSA.WIENER  import wiener_attack
from RSA.FERMAT import fermat



def parameters():

    print()
    print("Getting your RSA parameters...")
    multiple = input("Do you want to analyse multiple messages (y/n) ?\nAnswer:  ")
    if multiple == 'y':
        lst_mod = list(map(int,input("All the modulus separated by a space:  ").split()))
        lst_exp = list(map(int,input("All the exponent separated by a space:  ").split()))
        return multiple_messages(lst_mod, lst_exp)
    elif multiple == 'n':
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
        mess = input("What is your Ciphertext (decimal input) ?\nMessage:  ")
        try:
            message = int(mess)
        except ValueError:
            print("Error: Invalid Message Format")
            return
        print()
        print("Public key  and message successfully received!")
        print("Testing your parameters...\n")
        return check_params(modulus,exponent, message)
    else:
        print("Error: Invalid Answer")
        return

def multiple_messages(lst_mod, lst_exp):
    nb_modulus = len(lst_mod)
    nb_exp = len(lst_exp)
    if nb_exp != nb_modulus:
        print("You should have the same number of Modulus and exponent")
        return
    print("Individually Testing every parameters...\n")
    for i in range(nb_exp):
        check_params(lst_mod[i], lst_exp[i])
    return

    return
def check_params(N, e, m):
    print("Testing primality of the Modulus...")
    if isPrime(N):
        print()
        print(f"Your Modulus is a prime number which leads to an easy\ncomputation of the euler totient and your private key.")
        try:
            inv = inverse(e, N-1)
            print(f"Euler Totient = {N-1}\nPrivate key = {inv}")
            plain = pow(m,inv, N)
            print(f"decrypted message in decimal output= {plain}")
            print(f"decrypted message in bytes output= {long_to_bytes(plain)}")
        except ValueError:
            print("In fact, your exponent is not even invertible in the given Modulus\n")
        return
    print("Testing custom Wiener attack...")
    if wiener_attack(N,e, m):
        return
    print("Testing Fermat Factorization...")
    if fermat(N, e, m):
        return
    print()
    print("Your parameters were strong enough to pass CryptoResolve!\nBut always be careful when using RSA!")
    return




