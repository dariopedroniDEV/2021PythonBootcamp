mystring = "abcdefghijk"
# Grabbing first character of mystring with indexing
print(mystring[0])

# To grab the sentence part AFTER the 3rd character./
print(mystring[2:]) # = cdefghijk



# To get the first 4 characters om the left
mystring[:3] # = abc
print(mystring[:3])

mystring[3:6]
print(mystring[3:6]) # = def

mystring[::] # Will grab ALL the content
print(mystring[::])

# By using [::2] you can jump every two characters, taking acegik.
# You can mix start, stop and every X characters, like  this: [2:7:2] = ceg

mystring[::-1] # Will INVERT the content of a string.
print(mystring[::-1])
