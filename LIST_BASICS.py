#Lists

#lists are exactly what you expect. they are lists
#they are organized with index. This means starts at 0
# list can hold any data type

#example

#syntax
#[] this bracket makes a list.

my_stingy_landlords = ["Alfredo", "Betty", "Joanna", "Mr .Sumersbee", 123, True]
#            index    [    0         1       2            3]
#          neg index  [   -6        -5       -4          -3           -2     -1
#printing all of the list
print(my_stingy_landlords)

#access on entry of the list
#use the index with the list
# special = my_cringy_landlords [2]
# print(special)
#best way is as follows
print(my_stingy_landlords[2])

# #listclass
# print(type(my_cringy_landlords))
# #str class because [2] is a string
# print(type(my_cringy_landlords[2]))

#REASSIGN

my_stingy_landlords [-2] = "PAtty"
print(my_stingy_landlords)

my_stingy_landlords [-1] = "Hotel of mom and dad"
print(my_stingy_landlords)

#Remove an Entry from  a list
#remove hotel from list
#list.pop is set to pop the -1(the last one unless you specify)
my_stingy_landlords [-1] = "Hotel of mom and dad"
my_stingy_landlords.pop()
print(my_stingy_landlords)



#add to list
#Filipe to the list
#list.append is set by default to append at the last entry
my_stingy_landlords.append("Filipe")
print(my_stingy_landlords)

#remove from list
#.remove(object) is set by default to remove the first item  set to the value
my_stingy_landlords.append("Joanna")
print(my_stingy_landlords)

my_stingy_landlords.remove("Joanna")
print(my_stingy_landlords)






