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


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(direction,text,shift)