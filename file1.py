#Write a program that takes two numbers as input and prints their sum.
num1 = 10
num2 = 20
sum = num1 + num2
print("Sum of", num1, "and", num2, "is", sum)
#Write a python program that checks whether a given number is even or odd.
x = 46
if x % 46 == 0:
    print(x, "Is Even Number")
else:
    print(x, "Is Odd Number")
y = 71
if y % 71 == 0:
    print(y, "Is Even Number")
else:
    print(y, "Is Odd Number")
#Write a python program that calculates the factorial of a given number.
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
num = 7
print("Factorial of",num,"is",
factorial(num))
#Write a program that asks the user for their name and then prints a greeting message
user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Welcome to the prompt!")
#Write a program that takes a string input from the user and writes it to a text file.
user_input = input("Enter a string to write to the file: ")
file_name = "output.txt"
with open(file_name, "w") as file:
    file.write(user_input)
print(f"The string has been written to {file_name}")
#Write a program that reads the content of a text file and prints it to the console.
file_name = "output.txt"
try:
    with open(file_name, "r") as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
#Write a python program that takes a string as input and returns its length.
str = "yutika"
print(len(str))
#Write a python program that concatenates two strings and returns the result.
var1 = "My name "
var2 = "Is Yutika"
var3 = var1 + var2
print(var3)
# Write a python program that checks if a substring is present in a given string.
MyString1 = "Alaska is the largest state in the United States Of America"

if "largest" in MyString1:
	print("Yes!")
else:
	print("No!")
# Write a python program that converts a given string to uppercase.
real_text = "pie in the sky"
uppercase_text = real_text.upper()
print(uppercase_text)
#Write a python program that generates the first n numbers in the Fibonacci sequence.
def printFibonacciNumbers(n):
    f1 = 0
    f2 = 1
    if (n < 1):
        return
    print(f1, end=" ")
    for x in range(1, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next
printFibonacciNumbers(11)
#Write a python program that calculates the sum of the digits of a given number
def mySum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10
    return sum
n = 78912
print(mySum(n))
#Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
present_year = datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = present_year - birth_year
print("You are", age, "years old.")
#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines = []
print("Enter lines of text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("\nYou entered:")
for line in lines:
    print(line)
#Write a program that reads data from a CSV file and prints it to the console.








#Write a program in python that counts the frequency of each character in a string.
def count_character_frequency(input_string):
    char_frequency = {}
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency
input_string = input("Enter a string: ")
frequency_dict = count_character_frequency(input_string)
print("Character frequencies in the string:")
for char, freq in frequency_dict.items():
    print(f"{char}: {freq}")
#Write a program in python that converts a given string to title case (first letter of each word capitalized).
def to_title_case(input_string):
    return input_string.title()
input_string = input("Enter a string to convert to title case: ")
title_case_string = to_title_case(input_string)
print("Title case:", title_case_string)
#Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    return sorted(string1) == sorted(string2)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
#Write a python program that removes all punctuation from a given string.
import string
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)
input_string = input("Enter a string: ")
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:", cleaned_string)
#Write a python program that takes a list of numbers and returns their sum.
def sum_of_numbers(numbers):
    return sum(numbers)
input_string = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(float, input_string.split()))
total_sum = sum_of_numbers(numbers)
print("The sum of the numbers:", total_sum)
#Write a python program that counts the occurrences of a specific element in a list.
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count
lst = [1, 7, 4, 17, 11, 7, 10, 7, 9, 7]
x = 7
print('{} has occurred {} times'.format(x,
										countX(lst, x)))
#Write a python program that returns the minimum and maximum values in a list of numbers.
list1 = [2, 4, 6, 8, 10, 12];list2 = [1, 3, 5, 7, 9, 11]
x=[i for i in list1+list2]
print("maximum element is ",max(x),"minimum element is ",min(x))
#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input

celsius_1 = float(input("Temperature value in degree Celsius: "))
Fahrenheit_1 = (celsius_1 * 1.8) + 32
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'
      % (celsius_1, Fahrenheit_1))
print("----OR----")
celsius_2 = float(input("Temperature value in degree Celsius: "))
Fahrenheit_2 = (celsius_2 * 9 / 5) + 32
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'
      % (celsius_2, Fahrenheit_2))
#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice == '1':
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        result = n1 + n2
        print(f"{n1} + {n2} = {result}")
    elif choice == '2':
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        result = n1 - n2
        print(f"{n1} - {n2} = {result}")
    elif choice == '3':
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        result = n1 * n2
        print(f"{n1} * {n2} = {result}")
    elif choice == '4':
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        if n2 != 0:
            result = n1 / n2
            print(f"{n1} / {n2} = {result}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")
#Write a program that copies the contents of one text file to another.
def main():
    initial_file = input("Enter the path of the initial file: ")
    final_file = input("Enter the path of the final file: ")
    copy_file(initial_file, final_file)
    print(f"Contents copied from {initial_file} to {final_file} successfully.")
if __name__ == "__main__":
    main()
#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def main():
    input_string = input("Enter a string: ")
    prefix = input("Enter a prefix to check: ")
    suffix = input("Enter a suffix to check: ")
    if input_string.startswith(prefix):
        print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")
    if input_string.endswith(suffix):
        print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")
if __name__ == "__main__":
    main()
#Write a program in python that converts a string into a list of its characters.
def main():
    input_string = input("Enter a string: ")
    characters_list = list(input_string)
    print("List of characters:", characters_list)
if __name__ == "__main__":
    main()






























