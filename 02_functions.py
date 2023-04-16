username = 'DAniel Diaz Platon'

print(dir(username))

print()

# This is a comment

##########################
# This is another comment
##########################


'''
This is another comment for multilines
username
username
username

'''

# Data types
#
# List          -> [1,2,'aa']  It can be change 
# Tuple         -> (1,2,'aa')  It can not be change 
# Set           -> {1,2,'aa'}  
# Dictionaries  -> {'a': 1, 'b': 'hello'}

# multi line with the \ character
a = 1 + 2 + 3\
+5+6

print(a); print('Numbers:')

print('  Hello\n "world!!"')

print('Hello ' + 'world')

name = 'Daniel Diaz Platon'
age = 27
greeting_string = '\nHello Daniel, you are 27 years old\n'
greeting_string = '\nHello {}, you are {} years old\n'.format(name,age)
greeting_string_better = f'\nHello {name}, you are {age} years old\n'  # Add the character 'f' to add format
greeting_string_better = f'''\nHello {name}, 
you are {age} years old\n'''  # And with ''' inside of a variable means that you can write in different lines and it is valid
print(greeting_string_better)