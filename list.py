l1=[1,2,3,4]
l2=['one','two','three']
l3=[1,2,3,4,'sundar','tandam','caddcae']
print(l1)
print(l2)
print(l3)
print(type(l1))
print(type(l2))
print(type(l3))
print(l1[0])#postive indexing starts from zero
print(l2[2])
print(l3[4])
print(l1[-1]) #negative indexing starts from -1
print(l2[-3])
print(l3[-4])
#index slicing
print(l1[1:3])
print(l1[0:3])
print(l3[2:])
print(l1[:])
print(l2[:])
print(l3[:])
print(l3[-5:-1])
print(l2[-3:-1])
print('==============================================')
l4=l3.copy()
l5=l1+l2
print(l5)
print(l4)
l4.clear()
print(l4)