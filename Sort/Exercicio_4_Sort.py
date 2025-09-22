def count_lowercase_letters(word):
    counter = 0
    for letter in word:
        if 97 <= ord(letter) <= 122:
            counter += 1
    return counter

list_of_words = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

n =  len(list_of_words)

for i in range(n):
               for j in range(0, n - i -1 ):
                count_j = count_lowercase_letters(list_of_words[j])
                count_j_plus_1 = count_lowercase_letters(list_of_words[j + 1])

                if count_j > count_j_plus_1:
                    list_of_words[j], list_of_words[j + 1] = list_of_words[j + 1], list_of_words[j]

print(list_of_words)