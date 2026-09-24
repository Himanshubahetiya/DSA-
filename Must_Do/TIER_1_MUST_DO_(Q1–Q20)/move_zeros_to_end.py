# [0,1,0,3,12] → [1,3,12,0,0]
arr = [0,1,0,3,12,0,0,1,2,2,3,4,0,0,0,0,3,203,230,23,00,21]

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[j] == 0:
#             arr[j], arr[i] = arr[i], arr[j]


# print(arr)

j = 0 

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j+=1

print(arr)