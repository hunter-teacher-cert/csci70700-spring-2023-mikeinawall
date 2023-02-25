def encrypt(message):
  # encrypt function takes a only the message as a parameter
  # the overall goal of the function is to idenitfy the position of each character in the message and transpose them using the mod of their index value in the string. 


  #start with an empty string to concatenate the encryption to
  encryptText = ""

  #loop through the message by index
  for index in range(len(message)):
    #if the index is mod 0 ex: 0, 6, 12, 18,... then add the character in that index to encryptText
    if index % 6 == 0:
      encryptText += message[index]
  #add a space to seperate each chunk of letters
  encryptText += "   "

  #loop for mod 1
  for index in range(len(message)):
    if index % 6 == 1:
      encryptText += message[index]

  encryptText += "   "

  #loop for mod 2 
  for index in range(len(message)):
    if index % 6 == 2:
      encryptText += message[index]
      
  encryptText += "   "

  #loop for mod 3
  for index in range(len(message)):
    if index % 6 == 3:
      encryptText += message[index]

  encryptText += "   "

  #loop for mod 4
  for index in range(len(message)):
    if index % 6 == 4:
      encryptText += message[index]

  encryptText += "   "

  #loop for mod 5  
  for index in range(len(message)):
    if index % 6 == 5:
      encryptText += message[index]

  encryptText += "   "    
  return encryptText


def main():
  text = "MEETATTHREEPMTODAYATTHEUSUALLOCATION"
  #calling and printing of the encryption
  encrypted = encrypt(text)
  print(encrypted)

if __name__ == "__main__":
  main()