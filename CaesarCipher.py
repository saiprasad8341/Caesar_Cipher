alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Method 1
# ::::::::::::::::::::::::::::::::::::::
# def encrypt(plain_text, shift_amount):
#     cipher_test = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_test += new_letter
#     print(f"The encoded text is {cipher_test}")


# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")


# if (direction == "encode"):
#     encrypt(plain_text=text, shift_amount=shift)
# elif (direction == "decode"):
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Invalid input, Please try again..!")

# Method 2
# ::::::::::::::::::::::::::::::::::::::::::::
def caesar(text, shift_amount, direction):
    end_text = ""
    if (direction == "decode"):
        shift_amount *= -1
    for char in text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))

    if direction == "encode" or direction == "decode":
        shift = shift % 26
        caesar(text=text, shift_amount=shift, direction=direction)
    else:
        print(f"Invalid input {direction}, Please try again..!")

    result = input("Type 'yes' if you want to go again, Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye!!!")