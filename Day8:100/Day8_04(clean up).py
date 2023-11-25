alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


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

caesar(direction,text,shift)