x=int(input("Enter your range: "))
y=[]
for i in range (x):
    if i%2==0:
        y.append("*")
    else:
        y.append("#")
print(y)
