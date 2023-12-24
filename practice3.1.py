import random
count=int(input("Enter cout:  "))
num=[random.randint(0,10000)]
for i in range(count):
    num2=(random.randint(0,10000))
    if num2!=num[i-1]:
     num.append(num2)
    print(num)
