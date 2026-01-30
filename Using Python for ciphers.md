# Using Python in for ciphers

## Caesar cipher
> "Specifically, you will take each letter in your message, find its position in the alphabet, take the letter located after 3 positions in the alphabet, and replace the original letter with the new letter."

- indexes
- for loops
    "The iteration variable can have any valid name, but it's convenient to give it a meaningful name."
- lowercasing and uppercasing
- find.()


text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    index = alphabet.find(char)
    print(char, index)

---> char and index side by side


strings are imutable once created:
    my_string = 'brain'
    my_string[0] = 't'
^does not work.


You cannot change a string in a variable, but you can replace a string in a variable
    text = 'Hello World'
    text = 'Albatross'

It is better to create string variables outside loops if they get changed within a loop.

a = a + b -----> a += b


| Operator | Meaning                 |
| -------- | -------                 |
|  == 	   |Equal                    |
|  != 	   |Not equal                |
|   > 	   |Greater than             |
|   < 	   |Less than                |
|  >= 	   |Greater than or equal to |
|  <= 	   |Less than or equal to    |

The **%** operator returns the remainder of the division between two numbers.

If working with special characters, using the len() of the cipher is better than the int number of the characters in the cipher.

a function is a resuable block of code. starts with `def`, followed by the function name, and then ending with `():`. For example:
   
   `def function():`

variables defined outside a function have **global scope**.

variables defined inside a function have **local scope**.


functions can be declared with **parameters**, which are variables which can be used inside your function.

```python
def function_name(param_1, param_2):
    <code>
```

## Vigenere cipher
> "where the offset for each letter is determined by another text, called the key."

Each letter of the text is encrypted based on the position of each letter in the key. So, if we wanted to encrypt a, and the first letter of the key was x, then a would encrypt to x, because x is 24 positions away from a. Similarly, if we wanted to encrypt b and in the key the letter was s, b would encrypt to u, because u is 19 positions away from b, and s is the 19th letter in the alphabet (starting at position 0.)

comments explain the logic behind code.

`.index()` is similar to `.find()`, but if it is unable to find a substring, it throws a `ValueError`.

To account for wrap-around of the key, the % of len(key) is needed.

If you want to decrypt the message with the same function, make the function go backwards in how it determines the characters in the key. If you give the function an encrypted text, it decrypts back to the readable message based on the alphabet and the key.

Parameters can take default values. If no value is given in the function call for that parameter, the function will assume the default value assigned in it's definition.

The `.isalpha()` method returns `True` if a variable contains all letters.

`pass` can serve as a placeholder in incomplete functions with parameters.

Nesting functions on the final calling may be a cleaner way of writing code.

Two strings can join by using the `+` operator.

**f-strings** allow you to interpolate values into strings. This means that you can add variables with values into your strings. Such as:

`f"Hello, my name is {name}."` 

If a value is assigned to `name`, then displaying the f-string will pass the value into the string.

`\n` causes a new line when included in a string.