numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        print(f'{n} - ни простое, ни составное число')
        continue
    else:
        f = n ** (1 / 2)
    for j in range(2, int(f + 1)):
        if n % j == 0:
            is_prime = False
            break
    if not is_prime:
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True
print(f'Простые числа: \n{primes} ')
print(f'Составные числа: \n{not_primes}')
