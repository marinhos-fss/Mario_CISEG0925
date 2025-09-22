#Cria um dicionário vazio chamado 'produto'
produto = {}
#Adiciona os pares chave-valor ao dicionário
produto['nome'] = "Telemóvel"
produto['preço'] = 1500
produto['stock'] = 30
#Remove a chave 'stock' do dicionário
del produto['stock']
#Imprime o dicionário final
print(produto)