def sum_of_cubes_m_to_n(m, n):
    sum = 0
    for i in range(m, n + 1):
        sum += i ** 3
    return sum

m = int(input())
n = int(input())

result = sum_of_cubes_m_to_n(m,n)
print(result)