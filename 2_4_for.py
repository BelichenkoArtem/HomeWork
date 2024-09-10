numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# is_prime = True
for ind in range(len(numbers)):
    if numbers[ind] == 1:
        continue
    elif numbers[ind] == 2:
        primes.append(numbers[ind])

    else:
        for div in range(2, numbers[ind]):
            #print(div)
            if numbers[ind] % div == 0:
                 not_primes.append(numbers[ind])
                 break
        else:
            primes.append(numbers[ind])




# print('primes: ', list(set(primes)))
# print('not primes: ', list(set(not_primes)))
print('primes: ', primes)
print('not primes: ', not_primes)







