from Crypto.Util.number import inverse
import math

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
