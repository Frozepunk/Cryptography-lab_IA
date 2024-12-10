# Cryptography-lab_IA
## Ceasar cipher
### Source code 
```
def caesar_cipher():
    text = input("Enter text: ")
    key = int(input("Enter the key value: "))

    def shift(char, key, base, range_size):
        return chr((ord(char) - base + key) % range_size + base)

    # Encryption
    encrypted = ''.join(
        shift(char, key, ord('a'), 26) if char.islower() else
        shift(char, key, ord('A'), 26) if char.isupper() else
        shift(char, key, ord('0'), 10) if char.isdigit() else
        char
        for char in text
    )
    print("Encrypted text-->", encrypted)

    # Decryption
    decrypted = ''.join(
        shift(char, -key, ord('a'), 26) if char.islower() else
        shift(char, -key, ord('A'), 26) if char.isupper() else
        shift(char, -key, ord('0'), 10) if char.isdigit() else
        char
        for char in encrypted
    )
    print("Decrypted text-->", decrypted)

caesar_cipher()
```
## Rail Fence
### Source code 
```
def rail_fence_cipher(text, key):
    rail = [''] * key
    idx, step = 0, 1
    for char in text:
        rail[idx] += char
        idx += step
        if idx == 0 or idx == key - 1:
            step *= -1
    return ''.join(rail)

# User input
text = input("Enter the text: ")
key = int(input("Enter the key: "))

# encrypted = rail_fence_cipher(text, key)
# print("Encrypted text:", encrypted)

print(rail_fence_cipher(text, key))
```
## Vignear Cipher
### Source code 
```
def vigenere(text, key, decrypt=False):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    shift = -1 if decrypt else 1
    return ''.join(
        chr((ord(t) + shift * (ord(k) - 65) - 65) % 26 + 65) if t.isalpha() else t
        for t, k in zip(text.upper(), key.upper())
    )

# Example usage
text = input("Enter text: ")
key = input("Enter key: ")

encrypted = vigenere(text, key)
print("Encrypted text:", encrypted)

decrypted = vigenere(encrypted, key, decrypt=True)
print("Decrypted text:", decrypted)
```
## RSA
### Source code 
```
import math 
p=int(input("Enter the value of P:->"))
q=int(input("Enter the value of Q:->"))
n=p*q
phi_n=((p-1)*(q-1))
e=int(input("Enter the value of E:"))
while e<phi_n:
    if math.gcd(e,phi_n)==1:
        break
    e+=1
d=pow(e,-1,phi_n)
print(f"Public key ({e,n})")
print(f"Private key({d,n})")
m=int(input("Enter the value of M:"))
c=math.pow(m,e)%n
de=math.pow(c,d)%n
print(f"Encrypt{c}")
print(f"Decrypt {de}")
# inputs
# p = 3
# q = 5
# e = 2
# m = 4
```
