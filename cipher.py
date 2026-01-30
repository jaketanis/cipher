alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = 'Hello world!'
key = 'fanta'
key_index = 0
final_message = ''


lower_message = message.lower()

def converter(message,key):
    key_index = 0
    final_message = ''
    
    for char in lower_message:

        message_index = lower_message.find(char)

        if char.isalpha(): # used to convert

            alpha_index = alphabet.find(char)
            key_char = key[key_index % len(key)] # modulo of key length is used to account for wrap-around
            key_index += 1

            key_alpha_index = alphabet.index(key_char)
            new_index = (alpha_index + key_alpha_index % len(alphabet)) # modulo of alphabet length is to account for wrap-around

            new_char = alphabet[new_index]
            final_message += new_char

            print(char, new_char)
        else: # passes on symbols
            final_message += char
    return

converter(message,key)