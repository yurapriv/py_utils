# Use this to get file by full path
# import os
# os.path.join(os.path.expanduser('~'), 'file_name')


def generate_objc_strings_from_file(file_name):
    """
    Reads from file with name provided in file_name variable and
    prints every string in console with format '@"line_from_file"'.
    Printed strings can be used in objective-c code

    :param file_name: name of file to read
    """
    with open(file_name, 'r') as file:

        prefix = '@"'
        for line in file:
            line = line.strip(' \t\n\r')

            if len(line) == 0:
                print(line)
                continue

            if len(line) > 0 and line[-1] == ';':
                postfix = '"\n'
            else:
                postfix = ' "\n'

            new_line = prefix + line + postfix
            print(new_line, sep='', end='')

    return


generate_objc_strings_from_file('input.txt')
