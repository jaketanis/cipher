# global variables
alphabet = 'abcdefghijklmnopqrstuvwxyz'

final_message = ''

# inputs
choice = input("Encrypt or decrypt? \n")

key = input("\nWhat is the key? \n")

message = input("\nMessage: \n")

# functions
def converter(message, key, direction=1):

    lower_message = message.lower()
    key_index = 0
    final_message = ''

    for char in lower_message:
        if char.isalpha(): # used to convert
            alpha_index = alphabet.find(char)
            key_char = key[key_index % len(key)] # modulo of key length is used to account for wrap-around
            key_index += 1

            key_alpha_index = alphabet.index(key_char)
            new_index = (alpha_index + key_alpha_index*direction) % len(alphabet) # modulo of alphabet length is to account for wrap-around

            new_char = alphabet[new_index]
            final_message += new_char
        else: # passes on symbols
            final_message += char
    return print(final_message)

def encrypt(message, key):
    print("Encrypted message: \n")
    return converter(message,key)

def decrypt(message, key):
    print ("Decrypted message: \n")
    return converter(message, key, -1)

# outputs
if choice == "encrypt":
    encrypt(message,key)

elif choice == "decrypt":
    decrypt(message, key)
