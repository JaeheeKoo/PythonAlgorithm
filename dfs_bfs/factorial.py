# 0!과 1!의 값은 1입니다.

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  #n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1) 
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))
print(factorial_recursive(5))
