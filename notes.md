# cipher.py

A cipher encrypter and decrypter that runs in the terminal.

I'm imagining a tool used by two kids who want to send secret messages to eachother through e-mail.

One kid enters their message into the program, encrypts it, and then copies and pastes that encrypted message into an email to their friend.

The other kid receives it, and then decrypts it with the same program.

I will use the Vigenere cipher.
 
**The Vigenere cipher** - Encrypts a character in a string based on a key. Each character's position in the message is determined by the character in the key of the same index position. The cipher changes the character the amount of positions the key's character of that index is within the alphabet. 

## What do we need?

### a key

In this situation, the key can be determined by the kids. This way other's couldn't decrypt their message through the software.

### alphabet

Plain old alphabet.

### A message

The message can be as long or as short as the person who writes it wants it.

### Inputs

Message and key. 

### Functions

A function can receive the message and the key. With it, it can determine the new key based on the alphabet.

get position from the key first

add the letter from that position into the new message

```python
new_message = ''
alphabet = 'abcdefghijklmnopqrstuvwxzy'
message = 'Hello!'
key = fanta

def converter(message, key):
    lower_message = message.lower()
    for char in lower_message:
        key[char] = 
        char_num = int(char)

        new_message += message[char_num] + alphabet.find(char)
```

 `x = fruits.index("cherry")` --> returns the int position of the item.

 I have had some trouble understanding what .index and .find takes in. But I realized they produce ints, and take in str.

 After experimenting with 'hello!', I learned that both .find() and .index() return the position of the first specified value. So, that's why 'l' was showing as `2` in both occurrances.

I learned that .count() returns the amount of specified values. So, I can check if   lower_message.`count(char)` is greater than 1. Then I can find the index by using `.find()`, and start the search after `char`.

This may not even be an issue when trying to convert the string.

I will ignore this for now, because I don't remember specifying this scenario in the exercise. Instead I will try to focus on the conversion.

I need to make the new index take into account the position of the key within the alphabet, and then add that many spaces to the message.

I realized that we need to make the index of the message based on the len(). But I'm not sure how to do that.



I looked into how to completed code handled getting the indexes and tried to recreate it. Mine is a little different, but seems to be working. Although I ran into an error (see left)