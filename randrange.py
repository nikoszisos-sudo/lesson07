from random import seed
from random import randrange
from datetime import datetime

my_list = []

for x in range(10): # prints 10 times everything under this line

    my_column = set()

    while len(my_column) < 2: # 2 random numbers from 10 to 19 adding 2 of 6 numbers in set
        my_column.add(randrange(10,20))
    #print(my_column)

    while len(my_column) < 4: # 2 random numbers from 20 to 39 adding 4 of 6 numbers in set
        my_column.add(randrange(20,40))
    #print(my_column)

    while len(my_column) < 5: # 1 random numbers from 1 to 9 even number adding 5 of 6 numbers in set
      my_num = randrange(1,10)
      if my_num % 2 == 0:
         my_column.add(my_num)
    #print(my_column)

    while len(my_column) < 6: # 1 random numbers from 40 to 49 odd number adding 6 of 6 numbers in set
        my_num = randrange(40, 50)
        if my_num % 2 != 0:
         my_column.add(my_num)
    my_list.append(my_column)
for my_stili in my_list:
    print(my_stili)