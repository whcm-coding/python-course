import os
f = open('sketch.txt')
str = f.readlines()
print(str)

for line in f:
    print(line)
f.close()

cwd = os.getcwd()
print(cwd)

os.chdir('../')
print(os.getcwd())

os.chdir(cwd)
print(os.getcwd())
try:
    f = open('sketch.txt')
    for line in f:
        #  if  line.find(':')  !=  -1:
        #  if  not  line.find(':')  ==  -1:
        try:
            (role,  line_spoken) = line.split(':',  1)
            print("role  is:  ",  role,  "\nline_spoken  is:  ",  line_spoken)
        except:
            pass
    f.close()

    # str = f.readline()
    # res = str.split(':')
    # print("role  is:  ",  res[0],  "\nline_spoken  is:  ",  res[1])
    # (role,  line_spoken) = str.split(':')
    # print("role  is:  ",  role,  "\nline_spoken  is:  ",  line_spoken)
    # f.close()
except:
    print('the  data  file  is  missing')


try:
    f = open('sketch.txt')
    for line in f:
        try:
            (role, line_spoken) = line.split(':', 1)
            print("role  is:  ", role, "\nline_spoken  is:  ", line_spoken)
        except ValueError:
            pass
    f.close()
except IOError:
    print('the  data  file  is  missing')
