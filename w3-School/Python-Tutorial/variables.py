# Python has no command for declaring a variable
x = 5
y = "Smart"
print(x)
print(y)

#Variables don't need to be declared by a certain type and can be changed once first set

a = "welcome"
a = 4
print(a)

# If you want to specify a data type, this can be done with CASTING

b = str(4) # will be "4"
b = float(4) # will be 4.0
b = int(4) # will be 4
print(b)

# You can get the data type of a variable by using type()
c = 7
d = "smile"
print(type(c))
print(type(d))

# Variables can be declared with single and double quotes.

# Variables are not case sensite a and A are two different variables.

# A variable can have a long name which is more desciptive or a short name like a letter.

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

'''
# Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Assign multiple values

e, f, g = ("elephant", "fish", "Gator")
print(e)
print(f)
print(g)

# One value to multiple variables
h = i = j = ("Gator don't take no shit! Ya feel me")
print(h)
print(i)
print(j)

# Output variables

#Pythons print() is used to output variables

