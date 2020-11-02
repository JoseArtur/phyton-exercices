# Write a program that read two numbers.
# Print the first for the second multiplication result.Utilize only the operators of sum and subtration to calculate the result.
# Remember that we can understand  the multiplication of two numbers as the sucessive sums of one of them.So, 4 x 5 = 5 + 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4
x=int(input("Type the first number: "))
y=int(input("Type the second number: "))
i=0
j=0
print(f"{x} x {y} =",end=" ")
if i+1==y:
        print(x,end=" ")
        i=i+10
while i< y :
    #print(f"{x}X{y}={(x,end="+")}")
    print(x,end=" + ")
    i=i+1
    if i+1==(y):
         print(x,end=" ")
         i=i+1
print("=",end=" ")
if j+1==x:
        print(y,end=" ")
        j=j+10
while j< x:
     print(y,end=" + ")
     j=j+1
     if j+1==(x):
         print(y,end=" ")
         j=j+1
         
