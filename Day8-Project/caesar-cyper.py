"""
This is a Caesar Cypher program that allows a user to encode
or decode a piece of text by moving its letters along the
alphabet by adding a particular shift number.

This is done using a char list with the alphabet and selecting
the current char of the word, finding its index and then 
adding the shift number and retrieving the letter in the alphabet
with that particular index.

To Decode a particular word, we perform the same action but we
subtract the shift_amount from the current index of a char.

We use the modulus to allow cyclic motion and wraparound to 
ensure no index error in the alphabet list of chars. No matter
the shift, we'll ensure it encounters no index error by turning
a linear data structure into a circle with no beginning or end.

Any char not in the alphabet such as whitespace or numbers are just
appended as normal.

After the initial activity , the user is prompted if he wishes
to continue cyphering. If not, the program ends.

"""

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            output_text += char
        else:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

is_done_with_function = False
while not is_done_with_function:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    is_valid_input = False
    while not is_valid_input:
        restart_preference = input("Type 'yes' if you want to go again. "
                                "Otherwise, type 'no'.\n" ).lower()
        if restart_preference == "no" or restart_preference == 'yes':
            is_valid_input = True
            if restart_preference == "no":
                is_done_with_function = True
        else:
            print("Please type 'yes' or 'no'.")
