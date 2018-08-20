x0=1./7.

x=x0 #1/7
print('{:.16f}'.format(x), "1/7")
x+=x0 #2/7
print('{:.16f}'.format(x), "2/7")
x+=x0 #3/7
print('{:.16f}'.format(x), "3/7")
x+=x0 #4/7
print('{:.16f}'.format(x), "4/7")
x+=x0 #5/7
print('{:.16f}'.format(x), "5/7")
x+=x0 #6/7
print('{:.16f}'.format(x), "6/7")
x+=x0 #7/7
print('{:.16f}'.format(x), "7/7")
print('{:.9f}'.format(x), "7/7")

print(x==1.)
print(abs(x-1.)<0.00000001)

