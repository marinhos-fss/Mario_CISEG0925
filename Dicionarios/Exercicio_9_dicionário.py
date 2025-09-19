notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}


#Itera sobre cada aluno e suas notas
for aluno, lista_notas in notas.items():
    #Inicializa uma variável para a soma
    soma_notas = 0
    
    # Usa um loop para somar as notas uma a uma
    for nota in lista_notas:
        soma_notas += nota
    
    #Número de notas para a divisão
    numero_de_notas = len(lista_notas)
    
    # Calcula a média
    media = soma_notas / numero_de_notas
    
    # Imprime o resultado formatado
    print(f"{aluno}: {media:.1f}")