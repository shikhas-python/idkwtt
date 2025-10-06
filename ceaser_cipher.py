alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '()', ':', ';', "'", '"', '<', '>', ',', '.', '?', '/', '=', '+', '-', '_', ' ']

direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))



def ceaser(original_text, shift_amount, encode_or_decode):
       cipher_text = ""
       for letter in original_text:
               if letter == numbers or symbols :
                       cipher_text += letter
               else:
                     if encode_or_decode == "decode":
                       shift_amount *= -1
                       encoded_letter = alphabet.index(letter) + shift_amount
                       encoded_letter %= 25
                       cipher_text += alphabet[encoded_letter]
            
            
       print(f"here is the {encode_or_decode}d text: {cipher_text}")

ceaser(text, shift, direction)







         
    
         
        















