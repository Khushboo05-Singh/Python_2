# # 1. Write a python script to convert a number into str type
x=5
print(type(str(x)))

# 2. Write a python script to print Unicode of the character ‘m’
print(ord("m"))

# 3. Write a python script to print character representation of a given unicode 100.
print(chr(100))

# 4. Write a python script to print any number and its binary equivalent
a=5
print(bin(a))
print(hex(a))
print(oct(a))

# 7. Write a python script to store binary number 1100101 in a variable and print it in
# decimal format.
x="1100101"
a=int(x,2) 
print(a)

binary_number = '1100101'
decimal_number = int(binary_number, 2)
print(decimal_number)

# 8. Write a python script to store a hexadecimal number 2F in a variable and print it in
# octal format.
x="2F"
y=int(x,16)
z=oct(y)
print(z)

hex_number = '2F'
decimal_number = int(hex_number, 16)
octal_number = oct(decimal_number)
print(octal_number)

# 9. Write a python script to store an octal number 125 in a variable and print it in binary
# format.
x=oct(125)
y=int(x,8)
z=bin(y)
print(z)

# Store the octal number
octal_number = 0o125

# Convert octal to decimal
decimal_number = int(str(octal_number), 8)

# Convert decimal to binary
binary_number = bin(decimal_number)

# Print the binary number
print(binary_number)

# 10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
# display the result in binary format

# Convert octal number to decimal
octal_number = int('25', 8)

# Convert hexadecimal number to decimal
hexadecimal_number = int('39', 16)

# Add the decimal numbers
decimal_sum = octal_number + hexadecimal_number

# Convert the decimal sum to binary
binary_sum = bin(decimal_sum)[2:]  # [2:] is used to remove the '0b' prefix from the binary string

# Display the binary sum
print("The sum in binary format is:", binary_sum)


