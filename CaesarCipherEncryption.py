def encrypt(text, shift):
        encrypted = ""

        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shifted = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted += shifted

            else:
                encrypted += char

        return encrypted


def decrypt (decrypt, shift):
    decrypted_text = ""

    for char in decrypt:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += shifted
        else:
            decrypted_text +=char


    return decrypted_text
        
     
############################################## MAIN ##############################################

stay = "y"

while stay == "y":
    answer = input("Welcome, are you here to Encrypt or decrypt? (e for encrypt, d for decrypt): ")

    if answer == "e":
        OGsentence = input("Please enter what you want to be encrypted:")
        shift = int(input("Please enter your shift value:"))

        encrypted_sentence = encrypt(OGsentence, shift)
        print ("Your encrypted sentence is: ", encrypted_sentence)    
        stay = input("Do you want to encrypt/decrypt again? (y for yes, n for no): ")



    elif answer == "d":
        decrypt_this = input("Enter your sentence you wish to decrypt: ")
        decrypt_shift = int(input("What was the shift amount?: "))
    
        decrypted_sentence = decrypt(decrypt_this, decrypt_shift)
        print("Your decrypted text is: ", decrypted_sentence)
        stay = input("Do you want to encrypt/decrypt again? (y for yes, n for no): ")
    
    else:
        print("Please enter either e or d.")

print("Thank you for using! Have a great day :)")









