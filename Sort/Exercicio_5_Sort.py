list_of_words= ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

groups = {}

for word in list_of_words:
    first_letter = word[0]

    if first_letter not in groups:
        groups[first_letter] = []
    groups[first_letter].append(word)

for initial_letter in groups:
    groups_list = groups[initial_letter]
    n = len(groups_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if groups_list[j] > groups_list[j + 1]:
                groups_list[j], groups_list[j + 1] = groups_list[j + 1], groups_list[j]

items_to_sort = list(groups.items())

n = len(items_to_sort)
for i in range(n):
    for j in range(0, n - i - 1):
        if items_to_sort[j][0] > items_to_sort[j + 1][0]:
            items_to_sort[j], items_to_sort[j + 1] = items_to_sort[j + 1], items_to_sort[j]


ordered_groups = dict(items_to_sort)

print(ordered_groups)