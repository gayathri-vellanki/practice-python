x=[10,20,30,40,50]
print(x[len(x)-2::])
print(x[0::])
print(x[::-1])
l=[]
for i in range(0,300):
    l.append(i)
print(l[::2])
for i in range(len(x)-1,-1,-1):
    print(x[i])

#To show list is mutable
lt=[0,1,2,3,4,5,6,7,8,9]
lt[7]= 10
print(lt)

#delete element from list
x=lt.remove(3)
print(lt)

#Searching a element from list

ele=10
for i in range(0,len(lt)):
    if lt[i]==ele:
        print
