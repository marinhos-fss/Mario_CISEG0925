listanome=["Gui","Pedro","Andorinha","Gui"]
i=0

#flags
flagigualdade=0
flagkeepindex = []
#procura na lista caso que tenha dois nomes iguais

nomeproc=input("nome to search: ")

while i<len(listanome):
    if listanome[i]== nomeproc:
        flagigualdade+=1
        flagkeepindex.append(i)
    i+=1
print(flagkeepindex)
print(flagigualdade)

if flagigualdade>0:
    print("name found")
else:
    print("name not found")