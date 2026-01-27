def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

num = int(input("Enter a number: "))
print("Fibonacci of", num, "is", fib(num))
