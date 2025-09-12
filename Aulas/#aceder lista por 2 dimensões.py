#aceder lista por 2 dimensões

listanome=["Gui","Pedro","Andorinha"]
i=0
it=0

while i<len(listanome):
    it=0
    while it<len(listanome[i]):

        # print(i,"-",it) #i rotaçao externa e it rotação interna

        #para ver as letras
        print(listanome[i][it])
        print("")
        it+=1
    i+=1
