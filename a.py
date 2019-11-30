import numpy as np

lines = [1000, 1000000]
names = ['1.txt', '2.txt']


f1 = open(names[0], 'wt')
f2 = open(names[1], 'wt')

line1 = '%d\r\n%d\r\n%d\r\n%d\r\n'%(3, 4, 9, 15)
f1.write(line1)
f2.write(line1)

s1=15
s2=15
for i in range(lines[1]-4):
    it1 = s1+np.random.randint(3)+1
    it2 = s2+np.random.randint(3)+1
    if i < lines[0]-4:
        f1.write('%d\n'%it1)

    f2.write('%d\n'%it2)
    s1=it1
    s2=it2

f1.close()
f2.close()
