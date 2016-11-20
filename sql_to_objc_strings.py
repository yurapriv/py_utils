# Use this to get file by full path
# import os
# os.path.join(os.path.expanduser('~'), """"PATH_TO_FILE""")

file_name = 'input.txt'

with open(file_name, 'r') as file:
    file.readline(10)

    prefix = '@"'
    for line in file:
        line = line.strip(' \t\n\r')

        if line[-1] == ';':
            postfix = '"\n'
        else:
            postfix = ' "\n'

        newLine = prefix + line + postfix
        print(newLine, sep='', end='')