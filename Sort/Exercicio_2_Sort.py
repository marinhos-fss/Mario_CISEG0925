#Lista para odrdenar
list_of_words = ["Python", "inteligência", "Aprender", "dados", "Rede"]

#Ordenação invertida da lista ignorando maiúsculas e minúsculas
list_inversed_words = sorted(list_of_words, key =str.lower, reverse=True)

#Resultado
print(list_inversed_words)