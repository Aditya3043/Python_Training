count1=0
count2=0
for i in range(1,6):
    num=int(input("Enter A Number "))
    if i%2==0:
        count1+=1
    else:
        count2+=1

print(count1)
print(count2)
