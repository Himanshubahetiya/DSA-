l = [12, 335, 1, 10, 34, 99]

largest = l[0]
second_largest = 0 

for i in range(len(l)):
    if l[i] > largest:
        second_largest = largest
        largest = l[i]
    elif second_largest < l[i] and largest > l[i]:
        second_largest = l[i]


print(second_largest)




