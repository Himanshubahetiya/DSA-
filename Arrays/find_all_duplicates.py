nums = [1,2,2,3,4,5,5,6,7]
# arr = []

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             arr.append(nums[i])

# print(arr)

seen = set()
arr = []

for num in nums:
    if num in seen:
        arr.append(num)
    else:
        seen.add(num)
print(arr)