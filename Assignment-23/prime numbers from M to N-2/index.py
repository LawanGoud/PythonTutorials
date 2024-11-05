def check_is_prime(m, n):
    # complete this function
    result = ""
    for i in range(m, n + 1):
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result += str(i) + " "
    return result.strip()
    
m = int(input())
n = int(input())

prime_numbers = check_is_prime(m, n) # Call the check_is_prime function

print(prime_numbers)