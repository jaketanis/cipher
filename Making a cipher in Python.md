# The "unbreakable" cipher
Lewis Carroll is often known as the author of the esteemed childrens story "Through the Looking Glass", but Carroll was also a prolific mathematician. Growing up, he was always creating puzzles and logic games, some of which are represented in the stories he wrote. In 1868, Carroll published a study called ["The Alphabet Cipher"](https://en.wikipedia.org/wiki/The_Alphabet_Cipher) which showcased his invention of, as you would guess, the Alphabet Cipher. This type of cipher is known as a Vign&#233;re cipher. In this study, he coined this type of cipher as "unbreakable".

The Vign&#233;re cipher encrypts a message based on a key. Each letter of the message changes based on the position of the letters within the key. The letters in the message shift based on the key's corresponding letters' position in the alphabet. For example:

> `message` is the message to encrypt and `key` is the key. Since `k` is the 10th letter in the alphabet (if `a` is considered as 0), and the letter `m` is the 12th letter, the first letter of the encrypted message is the 22nd letter, which is `w`. The fully encrypted message is `wiqceeo`.

What was once seen as unbreakable to Carroll is actually quite doable for us with a modern programming language such as Python. I recently created a script that two people could use to encrypt and decrypt messages with the Vign&#233;re cipher in a terminal. This was mostly inspired from freeCodeCamps first project in [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/#learn-list-comprehension-by-building-a-case-converter-program). After completing that project, I wanted to test my skills; so, I created my own script based on what I learned in the project tutorial.

I'm going to walk through how I created this script, what roadblocks I ran into, and what I learned in the process.

## Creating the Vign&#233;re cipher in Python

When I created this script, I intended to make it so that it could be easily used. I imagined two kids sending secret messages to eachother through text or email, using their own computer to run this script that decryps and encrypts the messages. I knew that this would require some user inputs, which was different from the project tutorial I went through. But I knew that the hardest part of the script would be to get the logic correct. So, I spent most of my time figuring that out.

To create the logic, I first defined what I needed to create the logic with. This included the alphabet, a key, and a message. The function would receive the message and the key, and then determine the new message based on that information. This looked something like this:

```python
new_message = ''
alphabet = 'abcdefghijklmnopqrstuvwxzy'
message = 'Hello!'
key = fanta

def converter(message, key):
```
This cipher does not take into account for capital letters, so I needed to convert the message string into all lower case. This is done through the `.lower()` function.

My next objective was to find the position of the letter in the alphabet. I also wanted to track the position of the letter in the message itself. Eventually, I realized I didn't need to track the position of the letter in the message to accomplish my goals, so I ended up removing this later.


