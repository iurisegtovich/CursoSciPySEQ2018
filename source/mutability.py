i=1
print(id(i))
j=i
print(id(j)) #same object
j+=1
print(id(j)) #new object

t=(1,2,)
#t_0+=1 TypeError tuple object does not support item assignment

l=[3,4,]
print(id(l))
L=l
print(id(L)) #same object
L[0]=5.
L+=[6.]
print(id(L))  #still the same object

(a,b,c)=L
