list1 = []
list2 = []

with open("input.txt") as file:
    for line in file:
        numbers = line.split('   ')
        
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

occurances = {}

for n in list2:
    if n in occurances:
        occurances[n] += 1
    else:
        occurances[n] = 1

sum = 0
for n in list1:
    if n in occurances:
        sum += occurances[n] * n

print(sum)