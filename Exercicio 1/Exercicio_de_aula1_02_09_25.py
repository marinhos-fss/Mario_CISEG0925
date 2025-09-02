import time
full_name = input("Enter your full name: ")
i = 0
valid_name = True

while i < len(full_name):
    character = full_name[i]
    
    if i == 0:
        if not 'A' <= character <= 'Z':
            valid_name = False
            print("Invalid name.")
            break
            
    elif full_name[i - 1] == ' ':
        if not 'A' <= character <= 'Z':
            valid_name = False
            
            break
        
    else:
        if not ('a' <= character <= 'z' or character == ' '):
            valid_name = False
            
            break
            
    i += 1
    time.sleep(0.5)

if valid_name:
    print("Valid name!")
else:
      print("Invalid Name.")
    

    





'''
if i < len(full_name):
    char = full_name[i]
    print(char)
    time.sleep(0.5)
    i += 1
'''