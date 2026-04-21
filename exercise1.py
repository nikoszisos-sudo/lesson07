N = 5
A = set()
for i in range(1,N+1):
    A.add(i)
print(A)

my_set = set()
for element in A:
    my_tuple = (element, element**2)
    my_set.add(my_tuple)
print(my_set)