import numpy as np;

arr=np.random.randint(1,100,size=(4,4));
sum1=0;
mean=0;
l=[]

print(arr);

for i in arr:
  sum1=arr.mean()
  for j in i:
    j=j*sum1
    l.append(j)

l1=np.reshape(l,newshape=(4,4))
print(l1)








