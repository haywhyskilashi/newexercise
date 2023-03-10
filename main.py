# exercise 1

def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2


result = multiplication_or_sum(20, 30)
print("the result is", result)

result = multiplication_or_sum(40, 30)
print("The result is", result)


# Exercise 2 = ask user to enter name and age, currentyear. print to say year they will
#        turn 100 years old

name = input("What is your name? ")
age = int(input("How old are you? "))
currentYear = int(input("Enter the current year "))

newYear = currentYear + (100 - age)
print("Your name is ", name)
print("You will be 100years old in the year" ,newYear)


# Exercise 3 = ask user fora number. depending if the number is even or odd
#           print outmessage to user

userInput = int(input("Enter any random number "))


if userInput % 2 == 0:
    print(userInput, " is an even number")
elif userInput % 4 == 0:
    print(userInput, "is an multiple of 4")
else:
    print(userInput, "is an odd number")

checkNum = int(input("Enter a number that you want to divide"))
divideNum = int(input("Enter a number to divide by"))

if checkNum % divideNum == 0:
    print(checkNum, "is divisible by", divideNum)
else:
    print(checkNum, "is not divisible by", divideNum)


# Exercise 3 = print elements that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
aList = []

for x in a:
    if x < 5:
        print(x)
# return list that contains only elemt lass than 5
print( [x for x in a if x < 5] )

# Exercise 4 = user input & print list of all divisors of that number
