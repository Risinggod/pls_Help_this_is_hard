user_input=input("write down a number")
user_input=int(user_input)

list1=list(range(0, user_input))

list2=list(x*x for x in list1)

print(list1)
print(list2)



