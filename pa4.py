# 1.2 --> Andre
def find_and_swap(words, word_one, word_two):
    for i in range(len(words)):
        if words[i] == word_one:
            words[i] = word_two
        elif words[i] == word_two:
            words[i] = word_one
    print(words)
find_and_swap(['red','green','blue'],'red','green')

# 1.3 --> Andre
def extract_endingpath_from_paths():
    