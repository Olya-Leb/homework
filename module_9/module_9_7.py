def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n <= 1:
            print("Ни простое и ни составное")
            return n
        k = 0
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                k+=1
        if k == 0:
            print("Простое")
        else:
            print("Составное")
        return n
    return wrapper

@is_prime
def sum_three(*nums):
    return sum(nums)

result = sum_three(2, 3, 6)
print(result)