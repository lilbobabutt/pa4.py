#Part 1.1: File Finding
def extract_hwk_from_paths(paths):
    p = []
    for n in range(len(paths)):
        CSE8A = paths[n].split("/")
        p.append(CSE8A[-1])
    return p


print(extract_hwk_from_paths(["/home/CSE8A/alex/Hwk1.pdf", "/home/CSE8A/naomi/Hwk1.mp4", "/home/CSE11/jeff/Hwk1.pdf"]))

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
    
