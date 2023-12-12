direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher = ""
    for letter in text:
        if letter.isprintable():
            ordval = ord(letter)
            cipherval = (ordval + shift) % 256
            cipher += chr(cipherval)
        else:
            cipher += letter
    print(f"The encoded text is {cipher}")

# DO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text,shift):
    output = ''
    for letter in text:
        dOrdVal = ord(letter)
        decryptval = dOrdVal - shift
        if decryptval > ord('z'):
            decryptval = ord('a') - shift + \
                        (ord('z') + dOrdVal - 1)
        output += chr(decryptval)
    print(f"The decoded text is {output}")
# DO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
# amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"


# DO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction'
# variable. Then call the correct function based on that 'drection' variable. You should be able to
# test the code to encrypt *AND* decrypt a message.
decrypt(text,shift)