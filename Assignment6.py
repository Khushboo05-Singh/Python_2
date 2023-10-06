# 1. Write a python script to check whether a given number is positive or non-positive
n=float(input("Enter the num:"))
if n > 0 :
   print("Num is positive")
else:
    print("Num is negative")

# 2. Write a python script to check whether a given number is divisible by 5 or not
n=float(input("Enter the num : "))
if n%5==0:
    print("Num is divisible by 5 ")
else:
    print("Num is not divisible by 5 ")

# 3. Write a python script to check whether a given number is even or odd
n=float(input("Enter the num: "))
if n%2==0:
    print("Num is even")
else:
    print("Num is odd")

# # 4. Write a python script to print greater between two numbers. Print number only once
# # even if the numbers are the same.
# n=float(input("Enter the num n : "))
# m=float(input("Enter the num m : "))
# if n>m:
#     print("num is greater m")
# elif m>n:
#     print("numis grester then n")
# else:
#     print("num is same ")

# 5. Write a python script to print two given words in dictionary order
def dictionary_order():
    word1=input("Enter the word1: ")
    word2=input("Enter the word2: ")
    words = [word1, word2]
    words.sort()
    #if word1>word2:
    print("  The Word is 1st visit",words)

dictionary_order()


"""# Take input from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Convert words to lowercase for case-insensitive sorting
word1 = word1.lower()
word2 = word2.lower()

# Create a list with the two words
words = [word1, word2]

# Sort the list in ascending order
words.sort()

# Print the words in dictionary order
print("Words in dictionary order:")
print(words[0])
print(words[1])
"""


