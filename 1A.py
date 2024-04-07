n=int(input("Enter the number of terms in fibonacci series : "))
a=0
b=1
c=0
for i in range(0,n):
    c=a+b
    a=b
    b=c

