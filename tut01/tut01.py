def factorial(x):
    if x==0:
        return 1
    else:
        return (x*factorial(x-1))

x=int(input("Enter the number whose factorial is to be found"))
ans=factorial(x)
print("The factorial of given number", x, "is", ans, ".")
