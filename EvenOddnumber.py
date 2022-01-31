n = int(input("Enter a range of number to count Even and odd numbers"))
count1=0
count2=0

for i in range(n):
    if i%2==0:
        count1+=1
    else:
        count2+=1
print("Even numbers are - ",count1)  
print("Odd numbers are - ",count2)