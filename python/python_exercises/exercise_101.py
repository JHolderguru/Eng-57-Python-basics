# # Define the following variables
# # # name, last_name, age, eye_color, hair_color
# first_name = input('')
# print(first_name)
# print(type(first_name))
# #
# last_name = ('')
# print((type(last_name))
#
# eye_color = ('')
# print((type(eye_color))
#
# hair_color = ('')
# print((type(hair_color))
#
# age = ('')
# print((type(age))

# Prompt user for input and Re-assign these
import datetime

name = (input('what is your name? '))
print(name)

#last_name = (input('what is your last name? '))
# print(last_name)
#
# age = (input('what is your age? '))
# print(age)
#
# eye_color = (input('what is your eye_color? '))
# print(eye_color)
#
# hair_color = (input('what is your hair_color? '))
# print(hair_color)
#
# # Define the following variables
# print(type(name))
# print(type(last_name))
# print(type(age))
# print(type(eye_color))
# print(type(hair_color))
#
# # Print them back to the user as conversation
# # Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print('Hello ' + name + last_name + ' Welcome, your age is ' +
#       age + ' your eyes are ' + eye_color + ' and your hair color is ' + hair_color)

#Extra - Section 2 - Calculate in what year was the person born? and respond back.
# print something like: 'You said you we're 28 hence you were born in 1991!'
year = datetime.datetime.now().year
age = int(input('what is your age? '))
year_of_birth = (year - age)
print('You said you were ' + age + 'hence you were born in ' + year_of_birth)


#Extra - Cast your input
