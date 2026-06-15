def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
n = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter element value:"))
    arr.append(num)
result = is_sorted(arr)
if result:
    print("Array is sorted")
else:
    print("Array is not sorted")    