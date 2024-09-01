import numpy as np

arr1=np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]]);
l=[];
sum1=0

for i in arr1:
    for j in i:
        sum1=arr1.mean();

    l.append(sum1);

print(l)
