from RSA import RSA_main
from DHKE import DHKE_main
import ECC


def main():
    print()
    print("Welcome To CryptoResolve, a tool to test your use of different Cryptosystems.\n")
    chosen = input("Which cryptosytem/key exchange method do you want to analyze?\nOptions available are : RSA, ECC, DHKE.\nChoice:  ")
    if chosen in ["RSA", "Rsa", "rsa"]:
        RSA_main.parameters()
    elif chosen in ["DHKE", "Dhke", "dhke"]:
        DHKE_main.parameters()
    elif chosen in ["ECC", "Ecc", "ecc"]:
        ECC.parameters()
    else:
        print("Error: This is not a supported input")


main()
