arr = [1, 4, 7, 8, 9, 10]
m = 3

# sorting 
for i in range(len(arr)):
    for j in range(i+1 , len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

new_arr = []
count = 0
for i in arr:
    if count < m:
        new_arr.append(i)
        count +=1

min = new_arr[0]
max = new_arr[m-1]
print(max - min)