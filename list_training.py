def binarySearch(array, x : list, low, high):
    if high >= low:
        mid =low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return -1

k = []
j= 0
for i in range(1000000):
    k.append([i,j])
    k.append([i,j])
    j = j + 1
print(k)
input("bad enter time begirid")
new_k = []

i = 0

for elem in k:
    x = binarySearch(k,elem,i+1,len(k)-1)
    i = i + 1
    if x == -1:
        new_k.append(elem)
k = new_k
print(k)
