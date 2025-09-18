#Dicionário do exercicios
utilizador = {'nome' : 'Carlos' , 'idade' : 28}

#Chave para verificar
chave_a_verificar = 'email'

#Verificação da exestência da chave
if chave_a_verificar in utilizador:
    print(f"O email foi encontrado: {utilizador[chave_a_verificar]}")
else:
    print("Email não encontrado")