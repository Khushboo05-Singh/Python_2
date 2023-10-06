# 1. Writpython script to take your name as input from the 
# user and then print it
a=input("Enetr your name: ")
print("My name is ",a)

print("My name is ",input("Enter your name: "))

# 2. Write a python script to take input from the user.
# Input must be a number
a=int(input("Enter the num: "))
print(a)

# 3. Write a python script which takes two numbers from the user, then calculate their sum
# and display the result.
a=int(input("Enter the 1st num: "))
b=int(input("Enter the 2nd num: "))
sum=a+b
print("sum of two num is : ", sum)

# 4. Write a python script which takes the radius from the user and display area of a circle.
r=int(input("Enter the radis: "))
PI=3.142
area=PI*r*r
print("The area of circle is: ",area)

# 5. Write a python script to calculate the square of a number. Number is entered by the user.
n=int(input("The num is : "))
square=n**2
print("Squaare of this num is : ",square)

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
HALF=0.5
b=int(input("Enter the base : "))
h=int(input("enter the Height : "))
area=HALF*b*h
print("Area of Trangle is : ",area)

# 7. Write a python script to calculate average of three numbers, entered by the user
no1=int(input("Enter 1st value"))
no2=int(input("enter 2nd value"))
no3=int(input("enter 3rd value"))
average=no1+no2+no3/3
print("The average of Three num is: ",average)

no1=float(input("Enter 1st value"))
no2=float(input("enter 2nd value"))
no3=float(input("enter 3rd value"))
average=no1+no2+no3/3
print("The average of Three num is: ",average)

# 8. Write a python script to calculate simple interest
p=float(input("Enter profit value"))
r=float(input("enter rate value"))
t=float(input("enter time value"))
SI=p*r*t/100
print("Simple interest is :",SI)

# 9. Write a python script to calculate the volume of a cuboid
l=float(input("Enter leanth value: "))
b=float(input("enter breath value: "))
h=float(input("enter height value: "))
volume=l*b*h
print("The volume of cuboid",volume)

# 10. Write a python script to calculate area of a rectangle
l=float(input("Enter leanth value: "))
b=float(input("enter breath value: "))
area=l*b
print("Area of rectangle : ",area)






