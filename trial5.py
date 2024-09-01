import numpy as np

arr = np.random.randint(1, 10, size=(4, 4));
sum1 = 0
mean = 0
val1 = 0
print(arr.shape)
l = []
for i in range(len(arr)):
    for j in range(len(arr)):
        sum1 = arr.mean()
        val1 = sum1 * arr[i, j]

    l.append(val1)

l2 = np.array(l)
l3 = l2.reshape(2, 2)
print(l3)




