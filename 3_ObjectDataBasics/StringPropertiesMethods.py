""""
String elements are immutable.
This means that you cannot change the value of a single element inside a string.

One of the simplest solutions is to concatenate two strings and create a new one.
"""

# Original string:
name = "Sam"
# Changing the name from Sam to Pam:
last_letters = name[1:] # Grabs all letters AFTER letter 1.

'P' + last_letters # = Pam

