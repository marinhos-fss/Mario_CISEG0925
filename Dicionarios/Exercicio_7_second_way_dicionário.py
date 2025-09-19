d = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {}

for key, valor in d.items():
    inverted_dict[valor] = key

print(inverted_dict)