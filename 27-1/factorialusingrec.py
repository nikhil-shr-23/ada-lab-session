def fa(n):
    if n == 0:
        return 1
    else:
        return n * fa(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", fa(num))


