from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes


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
    print("Testing your parameters...")

