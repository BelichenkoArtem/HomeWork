numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# is_prime = True
for val in numbers:
    if val == 1:
        continue
    elif val == 2:
        primes.append(val)

    else:
        for div in range(2, val):
            #print(div)
            if val % div == 0:
                 not_primes.append(val)
                 break
        else:
            primes.append(val)




# print('primes: ', list(set(primes)))
# print('not primes: ', list(set(not_primes)))
print('primes: ', primes)
print('not primes: ', not_primes)







