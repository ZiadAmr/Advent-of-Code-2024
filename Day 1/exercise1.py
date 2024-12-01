list1 = []
list2 = []

with open("input.txt") as file:
    for line in file:
        numbers = line.split('   ')
        
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

list1.sort()
list2.sort()

pairs = zip(list1, list2)

sum = 0
for pair in pairs:
    sum += abs(pair[0] - pair[1])

print(sum)