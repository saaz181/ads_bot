import re

filename = 'dummy.txt'

pattern = r"'(.*?)'"

with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n').strip()
        var_name = line.replace('-', '_')
        string = f'{var_name} = carved_out_keyword.get("{line}")\n'
        with open('dummy1.txt', 'a') as f1:
            f1.write(string)