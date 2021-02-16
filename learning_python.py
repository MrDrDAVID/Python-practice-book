file_name = 'stuff_i_learned_in_python.txt'

print('This method prints out the whole flie at once.')
with open(file_name) as file_object :
    print(file_object.read())

print()

print('This method prints out the file line by line in a for loop.')
with open(file_name) as object_file :
    for line in object_file :
        print(line.replace('python', 'C'))

print()


print('This method prints out the file by putting it in a list and using outside the with block.')
with open(file_name) as file_obj :
    file_list = file_obj.readlines()

for line in file_list :
    print(line.rstrip())
