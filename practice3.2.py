x=int(input("Enter count: "))
numbers=[]
for i in range (x):
    y=int(input("Enter number: "))
    numbers.append(y)


numbers2=numbers[:]
numbers2.sort()
if numbers2==numbers:
    print("its ok,thanks")
    print(numbers)
    print(numbers2)
else:
     print("good job",numbers2)
     print("try again",numbers)
   
   
