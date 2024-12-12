alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text=""
    for letter in original_text:
        shift_pos = alphabet.index(letter)+shift_amount
        shift_pos %= len(alphabet)
        encrypted_text += alphabet[shift_pos]

    return encrypted_text
        
def decrypt(decripted_text, shift_amount):
    original_text=""
    for letter in decripted_text:
        shift_pos = alphabet.index(letter)-shift_amount
        shift_pos %= len(alphabet)
        original_text += alphabet[shift_pos]

    return original_text

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message\n").lower()
shift = int(input("Type the shift number\n"))
enc_result = encrypt(text,shift)
dec_result = decrypt(enc_result,shift)
print(enc_result)
print(dec_result)

    
