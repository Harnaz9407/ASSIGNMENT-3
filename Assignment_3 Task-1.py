def factorial(n):
    if n<0:
        print("Factorial not defined")
    elif 0<n<2:
        return 1
    else:
        total=1
        for i in range(1,n+1):
            total = total * i
        return total
n=int(input("Enter a number: "))
result=factorial(n)
print("Factorial of ",n,"is: ",result)
