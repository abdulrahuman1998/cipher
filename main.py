alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def encrypt(text,shift):
  cipher_text=""
  for letter in text:
    index=0
    new_index=0
    index=alphabet.index(letter)
    new_index=(index + shift)%26
    cipher_text+=str(alphabet[new_index])
  print(f"The Encoded result is {cipher_text}")





def decrypt(text1,shift1):
  plain_text=""
  for letter in text1:
    index=0
    new_index=0
    index=alphabet.index(letter)
    new_index=(index - shift1)%26
    plain_text+=str(alphabet[new_index])
  print(f"The decoded result is {plain_text}")



from art import logo
print(logo)
choice="yes"
while choice=="yes":

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text,shift)

  elif direction == "decode":
    text1 = input("Type your message:\n").lower()
    shift1 = int(input("Type the shift number:\n"))
    decrypt(text1,shift1)
  
  else:
    print("### Invalid input ###")
    quit()

  a=input("Type 'yes' if you want to go again. Otherwise 'no'")
  if a=="yes":
    choice == "yes"
  elif a=="no":
    choice == "no"
  else:
    print("## Invalid Input ##")
    quit()
    