print('Control flow lesson')

# || or
# && and
print(5 == 5 and 3==2)

# ! not
print(not 5 == 5)



# current_language = input('What language are you learning: ')

# if current_language == 'python':
#     print('You are learning unit 4')
# elif current_language == 'javascript':
#     print('You are learning unit 1,2, or 3')
# else:
#     print('You are in the wrong Class')



print('---------------')
print('Looping')

# i will start at 0 and stop at 5 (NOT INCLUDING 5)
for i in range(5):
    print(i)

print('---------------')

# i will start at 2 and stop at 5 (NOT INCLUDING 5)
for i in range(2,5):
    print(i)

print('---------------')

# i will start at 1 and stop at 10 (NOT INCLUDING 10) and go up by 3 every loop
for i in range(1,10,3):
    print(i)



# no matter what you take in input it will always be string
age = int(input('Please give your age: '))
print(age > 18)