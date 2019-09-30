import nester
import os

man = []
other = []
try:
    f = open('sketch.txt')
    for line in f:
        try:
            (role, line_spoken) = line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

#     try:
#         man_file = open('man_data.txt', 'w')
#         other_file = open('other_data.txt', 'w')
#         print(man, file=man_file)
#         print(other, file=other_file)

#         man_file.close()
#         other_file.close()
#     except:
#         print('save file error')
#     finally:
#         man_file.close()
#         other_file.close()
#     f.close()
except IOError:
    print('the  data  file  is  missing')


# out = open('data.txt', 'w')
# print('hello world', file=out)

# out = open('data.txt', 'a')
# print('hello world', file=out)
# out.close()
with open('man_data_lol.txt', 'w') as mdf:
    nester.print_lol(man, False, 0, mdf)
