# CryptoResolve (Currently in Development)

## CryptoResolve is a tool to secure the use of well-known cryptosystems and key exchange methods (RSA, ECC, DHKE...) by identifying possible attacks on the parameters that you are using.

# Installation
 Clone the Repository :
  ```bash
  git clone https://github.com/fr0mars/CryptoResolve/
  cd CryptoResolve/
  ```
# Usage
 CryptoResolve works from command line so just launch solver.py
```bash
cd src/
python3 solver.py
```

# Available Attacks (12/23)
  ## RSA
  ### - Fermat factorization attack on the Modulus (09/23)
  ### - Wiener attack on small private keys (09/23)

  ## Diffie-Hellman
  ### - Bruteforce on small keys with Baby Step Giant Step algorithm. (09/23)

# Incoming ...
  ### - Attack on multiple message with low exponent (CRT) (12/23)
