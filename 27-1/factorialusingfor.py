num = int(input("number enter crow"))
fact = 1

if num<0:
    print("no negative numvers")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact * i
    print("factorial of",num,"is",fact)