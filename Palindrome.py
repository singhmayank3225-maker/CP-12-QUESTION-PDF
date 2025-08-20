a=int(input("enter the no : "))
n=a 
sum=0
while(n>0):
    i=n%10
    n=n//10
    sum=sum*10+i
if(a==sum):
    print("Yes")
else:
    print("No")