def ceasar_cipher_func():
    text=input("Enter the text \n")
    key=int(input("Enter the key value \n"))
    def shift(char,key,base,range_size):
        return chr((ord(char)-base+key) % range_size +base)
    encryption=''.join(
        shift(char,key,ord('a'),26) if char.islower() else
        shift(char,key,ord('A'),26) if char.isupper() else
        shift(char,key,ord('0'),10) if char.isdigit() else
        char
        for char in text
    )
    print(encryption)
    decryption=''.join(
        shift(char, -key,ord('a'),26) if char.islower() else
        shift(char, -key,ord('A'),26) if char.isupper() else
        shift(char, -key,ord('0'),10) if char.isdigit() else
        char
        for char in encryption
    )
    print(decryption)
# main func calls
ceasar_cipher_func()