import time
# tabela ascII
# A-Z 65-90
# a-z 97-122
# space 32

full_name = input("Enter your full name: ")
i = 0
valid_name = True #Flag to indicate if the name is valid or not

#loop to check each character in the name
while i < len(full_name):

    character = full_name[i] #current character
    
    if i == 0:
        if not (65 <= ord(character)<= 90): #Must be upper case
            valid_name = False
            print("Invalid name.")
            break
            
    elif full_name[i - 1] == ' ': # Character after space
        if not (65 <= ord(character) <= 90): #Must be upper case
            valid_name = False
            break

    else: # Other characters
        if not (97 <= ord(character) <= 122) and character != ' ': #Must be lower case or space
            valid_name = False
            break
            
    i += 1
    time.sleep(0.5)

if valid_name:
    print("Valid name!")
else:
      print("Invalid Name.")
    
