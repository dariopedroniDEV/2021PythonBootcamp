# Avoid using as a Variable name Python keywords such as str or int.
# Write as much lowercase as possible and avoid starting a variable name with a number.


# In Python it is possible to change the data type of an already existing Variable.
# This is not possible with other programming languages (statically typed).

my_dogs = 2
my_dogs = ["Sammy", "Frankie"]

# Python automatically recognizes what data type does a variable contain, but in a language like C++ you need to
# declare the type while creating the variable.
# int my_dog = 1

# Dynamic Typing is easy to work with and fast. BUT may result in bugs for unexpected data types.
# Check out type()

# type(var) is used to see the value of a variable.
a = 10
print(type(a)) # The output will be 'int'

# Example of type() with a float value
a = 30.1
print(type(a))

