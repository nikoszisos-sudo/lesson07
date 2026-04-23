from random import seed
from random import randrange
from datetime import datetime

my_column = set()

my_randrange = randrange(10,20) # 2 random numbers from 10 to 19
my_column.add(my_randrange)
for i in range(1,2):
    while True:
        my_randrange = randrange(10,20)
        if my_randrange not in my_column:
            my_column.add(my_randrange)
            break
print(my_column)

my_randrange = randrange(20,40) # 2 random numbers from 20 to 39
my_column.add(my_randrange)
for i in range(1,2):
    while True:
        my_randrange = randrange(20,40)
        if my_randrange not in my_column:
            my_column.add(my_randrange)
            break
print(my_column)

while True:
    my_randrange = randrange(1, 10)  # 1 random numbers from 1 to 9 even number
    if my_randrange % 2 == 0:
     my_column.add(my_randrange)
     break
print(my_column)

while True:
    my_randrange = randrange(40, 50)  # 1 random numbers from 40 to 49 odd number
    if my_randrange % 2 != 0:
     my_column.add(my_randrange)
     break
print(my_column)