n=int(input("Enter a number"))
a=0
b=1
print("The Fibonacci series upto",n)
print(a)
print(b)
for i in range(0,n-2):
    c = a + b
    a = b
    b = c
    print(c)