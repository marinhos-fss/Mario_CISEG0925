#Introduz iuma palavra
word = input("Intoduza uma palavra: ")

#Add dicionário
letters_count = {}

for letra in word:
    if letra in letters_count:
        letters_count[letra] +=1 
    else:
        letters_count[letra] = 1
        
print(letters_count)


