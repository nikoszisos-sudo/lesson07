from random import seed
from random import randrange
from datetime import datetime

for x in range(10): # prints 10 times everything under this line

    my_column = set()

    while len(my_column) < 2: # 2 random numbers from 10 to 19
        my_column.add(randrange(10,20))
    #print(my_column)

    while len(my_column) < 4: # 2 random numbers from 20 to 39
        my_column.add(randrange(20,40))
    #print(my_column)

    while len(my_column) < 5: # 1 random numbers from 1 to 9 even number
      my_num = randrange(1,10)
      if my_num % 2 == 0:
         my_column.add(my_num)
    #print(my_column)

    while len(my_column) < 6: # 1 random numbers from 40 to 49 odd number
        my_num = randrange(40, 50)
        if my_num % 2 != 0:
         my_column.add(my_num)
    print(my_column)