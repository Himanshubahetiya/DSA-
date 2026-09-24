# Example: [1,1,2,2,3] → 3 (array becomes [1,2,3,...])
arr = [1,1,2,2,3,3,4,5,6,6]

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr)




