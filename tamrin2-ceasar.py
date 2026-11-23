#تمرین اول : الگوریتم سزار توسعه یافته 
def encrypt(text, k):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + k) % 26 + start)
            result += new_char
        else:
            result += char

    return result


def decrypt(text, k):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start - k) % 26 + start)
            result += new_char
        else:
            result += char

    return result


choice = input("1- Encrypt or 2- Decrypt: ")

text = input("Enter text: ")
k = int(input("Enter k: "))

if choice == "1":
    print("Result:", encrypt(text, k))

elif choice == "2":
    print("Result:", decrypt(text, k))

else:
    print("Wrong!")