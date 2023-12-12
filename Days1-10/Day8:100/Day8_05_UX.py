from Day8_art import logo


def caesar(direction, text, shift):
    cipher = ''
    if direction == "encode":
        for letter in text:
            ordval = ord(letter)
            cipherval = (ordval + shift) % 256
            cipher += chr(cipherval)
    elif direction == "decode":
        for letter in text:
            dOrdVal = ord(letter)
            decryptval = dOrdVal - shift
            if decryptval > ord('z'):
                decryptval = ord('a') - shift + \
                             (ord('z') + dOrdVal - 1)
            cipher += chr(decryptval)

    print(f"The encoded text is {cipher}")
    if input("Go Again? (yes or no)") == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)


# DO-1: Import and print the logo from art.py when the program starts.
print(logo)
# DO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

caesar(direction,text,shift)