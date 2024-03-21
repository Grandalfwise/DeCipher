# The function is used at the start, it calls the questions function to ask questions and then asks which cipher you want to use
def start():
    questions()
    cipher_choice = input("Which Cipher would you like: ")
    if cipher_choice == "r":
        reverse()
    elif cipher_choice == "c":
        caesar()
    elif cipher_choice == "mc":
        morse()
    elif cipher_choice == "m":
        monoalphabetic()
    elif cipher_choice == "a":
        atbash()
    else:
        invalid = "Invalid Input"
        print(invalid)

def questions():
    username = input("Please enter the name of the person: ")
    cyphers_to_be_used = f"\n Hi {username}, there are multiple ciphers you can use to decipher this"
    cyphers_to_be_used = cyphers_to_be_used.title()
    print(cyphers_to_be_used)
    ciphers = "Here are your choices: Reverse (r), Caesar (c), Morse Code (mc), Monoalphabetic (m), and Atbash (a).\n"
    print(ciphers)


####### CIPHERS #######


def reverse():
    message = input("enter the encrypted message: ")
    reversed_string = message[::-1]  # Used to print the opposite
    print(reversed_string)

# += used to put the different characters into one string
def caesar():
    message = input("enter the encrypted message: ")
    result = ""
    s = 3
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += chr((ord(char)))
    print(result)

def morse():
    print("Invalid. This has not been finished.")

def monoalphabetic():
    message = input("enter the encrypted message: ")
    result = ""
    s = 13
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += chr((ord(char)))
    print(result)

# Dictionary to replace the different letters.
capital_atbash = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}
lower_atbash = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
                'f': 'u', "g": 't', 'h': 's', 'i': 'r', 'j': 'q',
                'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
                'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

def atbash():
    message = input("enter the encrypted message: ")
    cipher = ''
    for i in range(len(message)):
        char = message[i]
        # checks for space
        if char != ' ':
            # adds the corresponding letter from the dictionary
            if char.isupper():
                cipher += capital_atbash[char]
            elif char.islower():
                cipher += lower_atbash[char]
            else:
                cipher += chr((ord(char)))
        else:
            cipher += ' '

    print(cipher)

start()
