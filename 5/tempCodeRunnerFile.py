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
    try:
        man_file = open('man_data.txt', 'w')
        other_file = open('other_data.txt', 'w')
        print(man, file=man_file)
        print(other, file=other_file)
    except:
        print('save file error')
    f.close()
except IOError:
    print('the  data  file  is  missing')