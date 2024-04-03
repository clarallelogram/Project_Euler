import math

# Problem 1: 233168 for n = 1000

def sum_of_multiples_of_3_or_5(n):
    sum = 0
    for i in range(n):
        if i%5 == 0 or i%3==0:
            sum+=i
    return sum

# Problem 2: 4613732 for n = 4,000,000

def sum_of_even_fibs(n):
    sum = 2
    base_1 = 1
    base_2 = 2
    
    while base_2<=n:
        tmp = base_2
        base_2 += base_1
        if base_2%2==0:
            sum+=base_2
        base_1 = tmp
    return sum

# Problem 3: 6857 for n = 600851475143

import sys
sys.setrecursionlimit(300000)

def largest_prime_factor(n):
    for i in range(math.floor(math.sqrt(n)), 1, -1):
        if n%i == 0 and largest_prime_factor(i)==None:
            return i

# Problem 4: 906609

def largest_palindrome_product():
    largest_palindrome_product = 1
    for i in range(100, 1000):
        for j in range(100, 1000):
            is_palindrome = True
            p = i*j
            str_product = str(p)
            for k in range(len(str_product)):
                if str_product[k] == str_product[len(str_product)-1-k]:
                    continue
                else:
                    is_palindrome = False
                    break
            if is_palindrome and p > largest_palindrome_product:
                largest_palindrome_product = p
            
    return largest_palindrome_product
    
# Problem 6: 25164150 for n = 100

def sum_square_difference(n):
    sum_of_squares = 0
    square_of_sum = 0
    for num in range(1, n+1):
        square_of_sum += num
        sum_of_squares += num**2
    square_of_sum **= 2
    return abs(square_of_sum-sum_of_squares)
    
# Problem 7: 104743 is the n = 10001st prime

def nth_prime(n):
    nth = 0
    num = 2
    while nth < n:
        if largest_prime_factor(num) == None:
            nth_prime = num
            nth+=1
        num += 1
    return nth_prime
    
# Problem 10: 142913828922 is the sum of all primes below n = 2,000,000
# This method is very slow for large n. Instead, the Sieve of Eratosthenes should be used to check primality.

def summation_of_primes(n):
    summation = 2
    for num in range(3, n, 2):
        if largest_prime_factor(num)==None:
            summation += num
    return summation
    
# Problem 20:

def factorial_digit_sum(n):
    product = 1
    digit_sum = 0
    for num in range(1, n+1):
        product *= num
    product_str = str(product)
    for digit in product_str:
        digit_sum += int(digit)
    return digit_sum
    
    
    
    
    
    
    
    
    
    
    
    
  