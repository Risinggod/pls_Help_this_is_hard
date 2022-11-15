import matplotlib.pyplot as plt

list1=list(range(-20, 21,))
list2=[x*x for x in list1]

plt.plot(list1, list2)
plt.show()
