import time
# Control flow

#If statements work with booleans

#control flow dictates where the code will run, much like damns in real life
#In coding we do this with <if> functions and while loops. We are going to look at
# <if > functions

#If functions
#if function works with booleans( True or False)
# we usually use comparison operators to equate and compare objects, and
#result in Tru or false (booleans)

#syntax if function
#if <condition>:
#    block of code (section of code that runs)
##In python, block is defined by indetation

#logical and
#syntax
#<condition> and <condition>
#both sides need to result in tru to be TRUE

#LOGICAL OR
#syntax
#<condition> OR <condition>
# #one side need to result in true to be TRUE
# print(True or True)
# print(True or False)
# print(False or False)

weather = "stormy"
safety_alert = "blue"


if weather == "stormy" and safety_alert =="red":
    print("duck for cover")

elif weather == "rainy":
    #time.sleep(2)
    print("bring umbrella")

#elif <Second_condition>
     #run this block of code
elif weather == "stormy":
    print("Stay at home and watch the storm")

#else:
    #block of code
else:
    print("put on sunny lotion")

