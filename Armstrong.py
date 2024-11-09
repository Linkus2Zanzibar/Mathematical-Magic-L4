num=int(input(" enter a number "))
digits=len(str(num))
result=0
temp=num
while temp!=0:
    digit=temp%10
    result=result+digit**digits
    temp=temp//10
print(result)
if(num==result):
    print(num," Is an Armstrong number ")
else:
    print(num," Is not an Armstrong number ")