num1=int(input("enter a num"))
num2=int(input("enter a num"))

if num1<0 and num2<0:
    print("enter a positive number")
else:
    sum=0
    while(num1>0 and num2>0):
        sum = num1+num2
        print("the sum is",sum)
        break
    
