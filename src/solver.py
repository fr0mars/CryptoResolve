from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse
import RSA
import DHKE
import ECC


def main():
    print()
    print("Welcome To CryptoResolve, a tool to test your use of different Cryptosystems.\n")
    chosen = input("Which cryptosytem/key exchange method do you want to analyze?\nOptions available are : RSA, ECC, DHKE.\nChoice:  ")
    if chosen in ["RSA", "Rsa", "rsa"]:
        RSA.test_parameters()
    elif chosen in ["DHKE", "Dhke", "dhke"]:
        DHKE.test_parameters()
    elif chosen in ["ECC", "Ecc", "ecc"]:
        ECC.test_parameters()
    else:
        print("Error: This is not a supported input")


main()
