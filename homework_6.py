#Homework 6
#1. Write a math quiz program that asks students questions on addition, subtraction, multiplication and
#division. The program randomly generates 2 numbers and randomly selects an operator and asks
#333 + 567
#The correct answer is 900. If the answer from the user is correct, it prints out congratulations. If not, it
#prints out the correct answer and a few words of encouragement.
import random
signs = ['+', '-', '*', '/']
first_number = random.randint(100, 999)
second_number = random.randint(100, 999)
sign = random.choice(signs)
if sign == '+':
  operation = 'plus'
  answer = float(first_number) + float(second_number)
  statement = "The First number: {}, The Second Number: {}\nWhat is {} + {} = ?".format(first_number, second_number, first_number, second_number)
  print(statement)
elif sign == '-':
  operation = 'minus'
  answer = float(first_number) - float(second_number)
  statement = "The First number: {}, The Second Number: {}\nWhat is {} - {} = ?".format(first_number, second_number, first_number, second_number)
  print(statement)
elif sign == '*':
  operation = 'multiplied by'
  answer = float(first_number) * float(second_number)
  statement = "The First number: {}, The Second Number: {}\nWhat is {} * {} = ?".format(first_number, second_number, first_number, second_number)
  print(statement)
elif sign == '/':
  operation = 'divided by'
  answer = float(first_number) / float(second_number)
  statement = "The First number: {}, The Second Number: {}\nWhat is {} / {} = ?".format(first_number, second_number, first_number, second_number)
  print(statement)
print("Statement: {}".format(statement))
quiz_answer = float(input("What is the answer to this question?"))
print("Quiz Answer: {}".format(quiz_answer))
print("Answer: {}".format(answer))

if answer == quiz_answer:
  print("Congratulations! You got the answer correct: {}".format(answer))
else:
  print("Close, but no cigar. Your answer of {} was incorrect. The correct answer is {}".format(quiz_answer, answer))

#2. Write a function that accepts a word (string) and prints out whether the word is a palindrome. This
#function does not need to return anything.
#(Hint: Use [::-1])
#palindrome(“happy”)
#This word is not a palindrome
#palindrome(“hannah”)
#This word is a palindrome

my_string = "racecar"
def palindrome(string):
  last = len(my_string)-1
  first = 0
  while first < last:
    if my_string[first] != my_string[last]:
      print("The string {} is not a palindrome!".format(my_string))
      break
    else:
      first += 1
      last -= 1
  if my_string[first] == my_string[last]:
    print("The string {} is MOST DEFINITELY a palindrome!".format(my_string))

palindrome(my_string)

#3. A hex number can only use these following characters “0123456789ABCDEF” (Hint: Use the in
#operator). Write a function called isHex(). It takes in a string and determines if the number is
#hexadecimal. It returns true or false

def isHex(hexnumber):
  import string
  result = string.ascii_letters
  length = len(hexnumber)
  good_digit_count = 0

  for i in range(0, len(hexnumber)):
    if hexnumber[i] in result[26:32] or int(hexnumber[i]) in range(0,10):
      print("Good So Far!")
      good_digit_count += 1
    else:
      print("Sorry! {} is not a properly formatted hexadecimal number!".format(hexnumber))

  if good_digit_count == length:
    print("Success! {} is a proper hexadecimal number!".format(hexnumber))
    return(True)
  else:
    print("Fail! This is NOT a properly formatted hexadecimal number!")
    return(False)


isHex("002B5C")

#4. Write a program that takes in a string of characters and returns the longest value-ascending string
#starting from the first position of the string. It means that, in the string, each subsequent character is
#greater than the previous one. Use the ASCII value table
#For example, ‘a’ is greater than “_” but it is smaller than “|”
#For example, given a string ”abcdefgzab” , it will return the longest string “abcdefgz” because it stops at
#the a after z

my_str = "abcdefgzab"

def ascii_length(str):
  my_str = "abcdefgzab"
  new_str = ""
  for i in range(0, len(my_str)):
    print("{} - {}".format(my_str[i], ord(my_str[i])))
    if int(ord(my_str[i])) < 122:
      new_str += my_str[i]
    elif int(ord(my_str[i])) == 122:
      new_str += my_str[i]
      print("Longest String in {}: {}".format(my_str, new_str))
      break
    elif ord(i) > 122:
      print("Longest String in {}: {}".format(my_str, new_str))

ascii_length(my_str)
