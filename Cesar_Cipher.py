# Entering the message you want to encrypt.
text = input("Input the message you want to encrypt: ")

# Inserting how many displacements there will be
dislocate = 0

while dislocate == 0:
    try:
        dislocate = int(input("Enter with the dislocate you want to encrypt: (1-25)"))
        if dislocate not in range(1,26):
            raise ValueError
        else:
            print(f"Value of displacement of {dislocate:.1f} accepted")
    except ValueError:
        dislocate = 0
    if dislocate == 0:
        print("Value incorrect, please input a new value between 0-26")

# Encrypting your message
crypt = " "

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code
        crypt_code = ord(char) + dislocate
        # Find if first letter is upper-case or lower-case
        if char.isupper():
            first = ord("A")
        else:
            first = ord("a")
        # Make correction
        crypt_code = (ord(char) - first + dislocate) % 26
        # Append the encoded character to the message
        crypt += chr(first + crypt_code)  
    else:
        crypt += char

print (f"Your message encrypting is: {crypt}")

