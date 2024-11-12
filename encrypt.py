def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(text, shift)
print("Encrypted text:", encrypted_text)
