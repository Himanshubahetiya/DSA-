nums = [1,2,3,5,8,8]

# broot force 
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             print(nums[i])



# best optimization 
slow = 0 
fast = 0 

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]

    if slow == fast:
        break 

slow = 0 

while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

print(slow)
