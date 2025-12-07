# Program to print all 2-digit prime numbers
# Total lines = 25

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("2-digit Prime Numbers:")

for num in range(10, 100):
    if isPrime(num):
        print(num)
