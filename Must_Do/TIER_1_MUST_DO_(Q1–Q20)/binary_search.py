arr = [1,2,3,4,5,6,7,8,9]
target = 7

low = 0
high = len(arr)-1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print(f"target found at index {mid}")
        break

    elif arr[mid] > target:
        high = mid - 1

    else :
        low = mid + 1

else:
    print("not found")