#Lista para ordenar
list_fruits= ['banana','uva', 'abacaxi', 'laranja']

#Ordenando a lista
def sorted_list(palavra):
    pri_caracter = palavra[0]
#Obter o valor numerico ASCII
    valor_ascii = ord(pri_caracter)

#97 = 'A' e 122 = 'z'
#Definindo prioridade para letras minusculas
    if 97 <= valor_ascii <= 122:
        priority = 0
    else:
        priority = 1
    return (priority, pri_caracter)

#Ordenação da lista a usar uma nova key definida 
list_ordenada = sorted(list_fruits, key = sorted_list)

#resultado
print(list_ordenada)
