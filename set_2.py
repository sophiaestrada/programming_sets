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
