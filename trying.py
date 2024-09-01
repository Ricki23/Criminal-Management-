import numpy as np

arr=np.random.randint(1,10,size=(4,4))

print(arr)

arr2=np.max(arr,axis=1)

print("\n\n")
print(arr2)

for x in range(len(arr)):
    for y in range(len(arr)):
        arr[x,y]=arr[x,y]*arr2[x]


print(arr)
