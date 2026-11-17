print('First Python Lesson')

# 1 line comment

my_name = 'Omar'


sayed_hamed_greeting = '''
Hello I am Hamed
I worked at escape room
I program
'''


'''
Multi
Line
Comment
'''

MAX_LOGIN_ATTEMPS = 3

print(MAX_LOGIN_ATTEMPS)


# prints the data type
print(type(my_name))

# python we have int and float
print(type(MAX_LOGIN_ATTEMPS))


# None: is the null data type
cpr_number = None


# Boolean: True or False
is_logged_in = False


# String concatenation
student_name='Mahdi'
course = 'Software Engineering'

print('Hi I am ' + student_name + ' And I am taking ' + course)
print(f'Hi I am {student_name} and I am taking {course}')



print(5*2)
print(5/2) # dividing always returns a float
print(5//2) # // returns an integer

my_num = 5
my_num += 2

print(my_num)


# methods same as javascript
print(my_name.upper())
print(my_name.lower())
print(my_name.capitalize())


# Arrays == List
students = ['Ali', 'Ali 2', 'Waleed']

print(students[2])

print('Ali' in students) # checks if 'Ali' String is in the List


# casting
test_number=4321
print(type(str(test_number)))

print(bool(test_number))

print(bool(0))

print(int(5.4))

# equality
print(5==3) # only == in python. NEVER ===
print(2==2)
print(3 != 4) # is 3 not equal to 4? True