# 1. Write a python script to remove the last digit from a given number. (for example, if
# user enters 2534 then your output should be 253)
n=int(input("Enter the num: "))
m=int(n/10)
print("After the remove last digits: ",m)

# 2. Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9)
n=int(input("Enter the num: "))
m=int(n%100)
print("The last digit of this num: ",m)

# 3. Write a python script to swap data of two variables
a=int(input("Enter the 1st num: "))
b=int(input("Enter the 2nd num: "))
a,b=b,a
print(a)
print(b)

# 4. Write a python script to find x power y, where values of x and y are given by user
x=int(input("enter the x value: "))
y=int(input("enter the y value: "))
power=x**y
print("x to the poder y values: ",power)

# 5. Write a python script which takes a three digit number from the user and displays
# only its first digit.
a=int(input("Enter the Three digit num: "))
b=int(a/100)
print(b)

# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.

a=int(input("Enter the Three digit num: "))
m=int(a%100/10)
print(m)

# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.
a=int(input("Enter the Three digit num: "))
l=int(a%10)
print(l)

# 8. Write a python script to use IN operator to display the data present in the list
#9. Write a python script to use NOT IN operator to display the data not present in l
list1=[1,2,3,4,5]
print(10 in list1)
print(3 in list1)
list2=[1,3,5,6]
print(2 not in list2)
print(3 not in list2)

# 10. Write a python script to use IS operator to display if both variables are the same
# object or not?
list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1 is list2)
print(list2==list1)
print(list2 is list1)







