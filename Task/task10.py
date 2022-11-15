sum1=0
sum2=0
for i in range(1,6):
    num=int(input("Enter A Number "))
    if num%2==0:
        sum1+=num
    else:
        sum2+=num

print("Sum Of Even Numbers :",sum1)
print("Sum Of odd Numbers :",sum2)
