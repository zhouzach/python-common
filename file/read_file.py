filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    # contents = file_object.read()

for line in lines:
    print(line.rstrip())

# print(contents)

