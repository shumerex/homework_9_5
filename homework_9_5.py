def is_prime(func):
    def wrapper(*args):
        def check_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) +1):
                if num % i == 0:
                    return False
            return True

        result = func(*args)
        if check_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result

    return  wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(6, 4, 11)
print(result)