#location = input('please enter the location in which you wanna create the file and file name? ')
operation = input('what operation would you like to perform\nfor read: \'r\'\nfor write: \'w\'\n')
filename = input('Enter the file name in which you wanna make changes? ')

if operation == 'w':
    print('Initiaing file writing operation...')
    file = open(filename, 'r')
    previous = file.readlines()
    file.close()
    file = open(filename, operation)
    for line in previous:
        file.write(line + '\n')
    content = input('hey enter the information to be updated in file: ')
    print('Writing into the file please wait...')
    file.write(content)
    file.close()
    print('the file is updated successfully...')
elif operation == 'r':
    print('Initiating file reading operation...')
    file = open(filename, operation)
    content = file.readlines()
    for line in content:
        if line[: -1] == '\n':
            print(line[:-1])
        else:
            print(line)
    file.close()
    print('File is readed successfully...')
else:
    print('hey please enter a valid operation...')