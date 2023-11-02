 #Write a program which, given two numbers, prints the sum of all even numbers between them (both inclusive).

def even_sum(num1, num2):
    sum = 0
    # Loop over all the numbers in the given boundary
    for x in range(num1, num2 + 1):
        # Only add the number x to the accumulative sum "sum" if the number is even (its x mod 2 = 0)
        if x % 2 == 0:
            # Add the even number to the sum
            sum += x
    return sum

#Collect user inputs

starting_num = int(input("Enter the starting number: "))
ending_num = int(input("Enter the ending number: "))

total_sum = even_sum(starting_num,ending_num)

print("The sum of all even numbers between", starting_num, "and", ending_num, "is", total_sum)

assert(even_sum(2,4) == 6)
assert(even_sum(2,3) == 2)
assert(even_sum(3,3) == 0)










#Write a program to test whether two strings are anagrams.

def is_anagram(str1, str2):

    # Remove all spaces in the given string and lowercase every alphabets 
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

user_string_1 = str(input("Enter a word or a sentence: "))
user_string_2 = str(input("Enter a word or a sentence: "))

if is_anagram(user_string_1,user_string_2) == True:
    print ('"',user_string_1, '" and "', user_string_2, 'are anagrams')
else:
    print ('"',user_string_1, '" and "', user_string_2, 'are not anagrams')

assert(is_anagram("Satan","Santa") == True)
assert(is_anagram("Tom Marvolo Riddle","I am Lord Voldemort") == True)
assert(is_anagram("ee","e") == False)










#A text file contains a list of integers, one per line. Write a script to print out the four most commonly occurring numbers, one per line, without surrounding whitespace.

import os
#Open a text file named "list_of_integers" in read mode
image = input("Enter file path or image data: ")

#check whether the specified path is an existing regular file or not.
if os.path.isfile(image):
    with open("list_of_integers.txt", "r") as integer_list:
        #list comprehension - strip removes all the whitespaces and line - the format is changed to integers to create a list of all the integers in the text file
        all_integers = [int(line.strip()) for line in integer_list]
    # Assign a dictionary to counter
    counter = {}
    #As we go through the list of numbers from the file, if the number is already in the dictionary as a key, we increase the value that corresponds to the key by one. If the number is not in the dictionary, we create a new dictionary key element and start counting from 1
    for i in all_integers:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    # Get the four most common numbers by sorting the dictionary in decreasing order of counter value
    most_common_numbers = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:4]

    # Print out the four most common numbers, one per line
    for number, count in most_common_numbers:
        print(number)

else:
    print("The file does not exist")










#Write a program to load an image from a file, take the 2D FFT of it, remove low-frequency components, and transform back. Feel free to use suitable libraries for the FFT.

import cv2
import numpy as np


# Image as greyscale
path = input("Enter a image file to manipulate")
image = cv2.imread(path, 0)

# Perform 2D FFT
f = np.fft.fft2(image)

#not sure how to remove lower frequency values here

final_img = np.fft.ifft2(f)
final_img = np.abs(final_img)










#Write a short piece of code in a language of your choice that demonstrates an interesting feature of, or effect in, that language. Please explain very briefly why you think it is interesting.

#timeit module implemented to calculate the running time between operations
from timeit import default_timer as timer

li = [51, 7, 22, 971, 514, 2, 17, 2314, 13, 62, 23]
 
#method 1 
start = timer()
final_list = list(map(lambda x: x*2, li))
end = timer()
print(end - start)

#method 2
start = timer()
for i in range(len(li)):
    li[i] = 2*li[i]
end = timer()
print(end - start)

#method 1 and 2 leads to the same output but method 1 uses map and lambda function to not only make the code more concise but also reduce the running time compared to using a standard for loop

#another interesting feature of Python is dynamic typing

x = 12
print(type(x))
x = 5.5
print(type(x))
x = True
print(type(x))
x = "cat"
print(type(x))
x = [1,2,3]
print(type(x))
x = (3,4,5)
print(type(x))

#Python automatically infers the data type and assigns it - variables can easily be reassigned to different data types without the need of new declarations
