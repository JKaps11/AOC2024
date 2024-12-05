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

# Sorting elements in each list
list_one.sort()
list_two.sort()

# Finding total distance
total_distance = 0

for i in range(len(list_one)):
    total_distance += abs(list_one[i] - list_two[i])

print(total_distance)
