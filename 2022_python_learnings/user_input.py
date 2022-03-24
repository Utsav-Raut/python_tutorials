# Taking numbers as input
beautiful_number = input("Enter a beautiful number:")
print(beautiful_number)
print(type(beautiful_number))

second_beautiful_number = float(input("Enter another beautiful number:"))
print(second_beautiful_number)
print(type(second_beautiful_number))

print("Big", 99, 1.2)
print("Big", 99, 1.2, sep=';')
print("Big", 99, 1.2, sep=';', end='!!\n')

for i in 'python':
    print(i, end=':')
print()

# Repeating characters
print("a"*5)

# ##################################################

# Taking multiple values as input
args = input('Enter the values\n').split()
print(args)

new_args = input('Enter another set of values\n').strip().split()
print(new_args)