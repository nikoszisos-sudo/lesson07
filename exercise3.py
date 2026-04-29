my_set_even = set(range(0, 101, 2))
print ("even numbers from 0-100: " + str(my_set_even))
print ("even numbers from 0-100 are : "+ str(len(my_set_even)) + " numbers")
my_set_odd = set(range(1, 101, 2))
print ("odd numbers from 0-100: " + str(my_set_odd))
print ("odd numbers from 0-100 are : "+ str(len(my_set_odd)) + " numbers")
my_set_multiple_3 = set(range(0, 101, 3))
print ("multiple 3 numbers from 0-100: " + str(my_set_multiple_3))
print ("multiple 3 numbers from 0-100 are : "+ str(len(my_set_multiple_3)) + " numbers")
my_list_primes = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        my_list_primes.append(i)
my_set_primes = set(my_list_primes)
print("prime numbers from 0-100 : "+ str(my_set_primes))
print("prime numbers from 0-100 are : "+ str(len(my_set_primes)) + " numbers")

my_set_even_or_multiple_3 = my_set_even | my_set_multiple_3
print("even numbers or multiple 3 from 0-100: "+ str(my_set_even_or_multiple_3))

my_set_odd_my_set_primes = my_set_odd & my_set_primes
print("odd numbers and primes from 0-100: "+ str(my_set_odd_my_set_primes))

my_set_primes_not_my_set_odds = my_set_primes - my_set_odd
print("prime numbers and not odds from 0-100: "+ str(my_set_primes_not_my_set_odds))

my_set_odd_symmetric_my_set_primes = my_set_odd ^ my_set_primes
print("odd numbers or primes but not odds and primes from 0-100: "+ str(my_set_odd_symmetric_my_set_primes))
