def caesar\_cipher\_encrypt(text, shift):
result = ""
for char in text:
if char.isalpha():
shift\_base = ord('A') if char.isupper() else ord('a')
result += chr((ord(char) - shift\_base + shift) % 26 + shift\_base)
else:
result += char  # Keep spaces and punctuation unchanged
return result

def caesar\_cipher\_decrypt(text, shift):
return caesar\_cipher\_encrypt(text, -shift)

def main():
print("Caesar Cipher Tool")
print("------------------")

```
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
if choice not in ['E', 'D']:
    print("Invalid choice. Please enter 'E' or 'D'.")
    return

message = input("Enter your message: ")
try:
    shift = int(input("Enter shift value (0-25): "))
    if not 0 <= shift <= 25:
        raise ValueError
except ValueError:
    print("Invalid shift value. Please enter a number between 0 and 25.")
    return

if choice == 'E':
    encrypted = caesar_cipher_encrypt(message, shift)
    print("Encrypted message:", encrypted)
else:
    decrypted = caesar_cipher_decrypt(message, shift)
    print("Decrypted message:", decrypted)
```

if **name** == "**main**":
main()   create a github repositary comment about the task simple language
