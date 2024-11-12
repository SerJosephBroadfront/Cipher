def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Enter text to decrypt: ")
shift = int(input("Enter shift value: "))

decrypted_text = decrypt(text, shift)
print("Decrypted text:", decrypted_text)
