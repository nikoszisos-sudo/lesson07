from random import randrange
N=28
my_students = set()
for i in range(N):
    my_students.add("student" + str(i))
print(my_students)

my_list_students = list(my_students) #convert to list
print(my_list_students)

for i in range(int(N/2)): #repeat N/2 times
    pos1 = randrange(0, len(my_list_students))
    student1 = my_list_students.pop(pos1)
    pos2 = randrange(0, len(my_list_students))
    student2 = my_list_students.pop(pos2)


    my_list_students.pop()
print(my_list_students)
