a=input("ride down a number for a")
b=input("ride down a number for b")
user_input1=int(a)
user_input2=int(b)

flist1=list(range(-20, 20))

list2=[a*x+b for x in flist1]

print(flist1)
print(list2)
