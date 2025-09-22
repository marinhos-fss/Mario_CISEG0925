# List to sort
list_of_words = ["Python", "inteligência", "Aprender", "dados", "Rede"]

def compare_words (word1, word2):
    
    '''Compares  tow words for invverse alphabetical sorting, ignoring case.
    Returns True if the first word is alphabetical smaller than the second word.
    '''
    # converts to lowercase for comparision
    word1_lower =  word1.lower()
    word2_lower =  word2.lower()

    # Use of < to sort in reverse order Z to A
    return word1_lower < word2_lower

# Bubble sort algorithm
n = len(list_of_words)  

#Outer loop: controls the passes through the list
for i in range(n):
    #Inner loop: compares and swaps adjacent elements
    for j in range (0, n - i -1):
        #Call the custom function to decide if a swap is needed
        if compare_words(list_of_words[j], list_of_words[j+1]):
            #Swap the elements if they are in the wrong order
            list_of_words[j], list_of_words[j+1] = list_of_words[j+1], list_of_words[j]

#Result
print(list_of_words)






'''
list_ofwords = []: This line simply the list of words to be sorted

def compare_words(...): This is a custom function that determines the order of two items

word1_lower = word1.lower(): To ignore case, the function converts both words to lowercase before comparing them

return word1_lower< word2_lower: Its to flip the logic. If word1 is alphabetical less than word, the function return rue. This tells the sorting algorithm that the words are in the wrong order and need to be swapped

n = len(list_of_words): The variable n stores the total number of words in the list, used to control the loop

for j in range (n): This is the outer loop of the bubble sort. It ensures the algorithm makes enough passes to fully sort the list.

for j in range (0, n-i-1): This is the inner loop. In each pass, it compares every pair of adjacent words. The n-i-1 part is small optimization to avoid re-checking elements that have been sorted already

if compare_words(list_of_words[j], list_of_words[j+1]): this is the swap condition. If the custom comparison functions returns true, the swap is executed

list_of_words[j], list_of_words [j+1] = list_of_words[j+1], list_of_words[j]: This line effecientlly swaps the positions of the words. The larger element bubbles into itsd correct place  in the list wich each pass.

print(list_of_words): Is just the result of the sorted list

'''
