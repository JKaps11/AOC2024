# Getting input into two lists
list_one = []
list_two = []

with open("aoc1input", "r") as file:
    for line in file:
        line = line.strip()
        cur_word = ""
        i = 0
        while i < len(line):
            if line[i] == " ":
                list_one.append(int(cur_word))
                cur_word = ""
                while line[i] == " ":
                    i += 1
            else:
                cur_word += line[i]
                i += 1
        list_two.append(int(cur_word))

# Calculating Similarity Score
similarity_score = 0

def freq(target):
    x = 0
    for num in list_two:
        if target == num:
            x += 1
    return x

for num in list_one:
    similarity_score +=  num * freq(num)

print(similarity_score)
