liste1=list(range(1, 101))
liste2=[x*x+x for x in liste1]

print(liste2),

list3=range(1, 101)

def math(x):
    return x*x+x

ergbnis=list(map(math, list3))

print(ergbnis)

