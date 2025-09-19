phrase = str(input("Introduza uma frase: "))

words = phrase.lower().split()

words_counting = {}

for word in words:
    words_counting[word] = words_counting.get(word,0) + 1

print(phrase)
print(words_counting) 