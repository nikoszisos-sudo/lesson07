from random import randrange
N=20
my_students = set()
for i in range(N):
    my_students.add("student" + str(i))

my_list_students = list(my_students) #convert set to list
my_math_teams = set() #create empty set of math teams
for i in range(int(N/2)): #repeat N/2 times
    pos1 = randrange(0, len(my_list_students)) #pick random position
    student1 = my_list_students.pop(pos1) #pop this student
    pos2 = randrange(0, len(my_list_students))
    student2 = my_list_students.pop(pos2)
    my_team = (student1, student2) #insert the 2 random pupils into a new tuple
    my_math_teams.add(my_team)
print("my math teams are: " + str(my_math_teams))

my_list_students = list(my_students) #convert set to list
my_geography_teams = set() #create empty set of geography teams
for i in range(int(N/2)): #repeat N/2 times
    pos1 = randrange(0, len(my_list_students)) #pick random position
    student1 = my_list_students.pop(pos1) #pop this student
    pos2 = randrange(0, len(my_list_students))
    student2 = my_list_students.pop(pos2)
    my_team = (student1, student2) #insert the 2 random pupils into a new tuple
    my_geography_teams.add(my_team)
print("my geography teams are: " + str(my_geography_teams))
