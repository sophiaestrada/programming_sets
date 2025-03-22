# no 1
def shift_letter(letter, shift):
  if letter == " ":
        return " "
  return chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))


# no 2
def caesar_cipher(message, shift):
  output = ""

  for letter in message:
    if letter == " ":
        output += " "
    else:
        output += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
  
  return output


# no 3
def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    return chr((ord(letter) - ord("A") + ord(letter_shift) - ord("A")) % 26 + ord("A"))


# no 4
def vigenere_cipher(message, key):
    output = ""  
    index = 0  

    for letter in message:
        if letter == " ":
            output += " "

        else:
            shift = ord(key[index]) - ord("A")
            new_letter = chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
            output += new_letter
            index = (index + 1) % len(key)  

    return output


# no 5
def scytale_cipher(message, shift):
    output = ""

    while len(message) % shift != 0:
        message += "_"  

    for i in range(len(message)):  
        index = (i // shift) + len(message) // shift  * (i % shift)
        output += message[index]

    return output


# no 6
def scytale_decipher(message, shift):
    output = ""

    for position in range(len(message)):
        og_position = (position // (len(message) // shift)) + shift * (position % (len(message) // shift)) # for reverse
        output += message[og_position]
    
    return output
