n=int(input("Enter the number : "))
fact=0
if n==0 or n==1:
    fact=1
    print(fact)
else:
    for i in range(2,n):
        fact=fact*i
        print(fact)
    
