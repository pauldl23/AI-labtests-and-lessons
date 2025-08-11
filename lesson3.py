#interative stratements

#for int x = 0; x<10 ; x++
for i in range (5):
    print(i, end = ' ')

for i in range(5,11):
    print(i, ' *', end=' ')

name = 'paul'

for c in name:
    print(c, end='+')

for i, value in enumerate (name):
    print(f'[{i}]={value}')

import time

#for i in range(1,11,1):
    #print(i, end= '')
   # time.sleep(0.5)


start, end = int(input('enter start: ')), int(input('enter end: '))
for i in range(start, end, 1):
    print(i, end = ' ')
    time.sleep(1)

#import random, time

#xfrom, xto = int(input('from: ')), int(input('to: '))
#howmany = int(input('how many: ')) + 1
#for x in range(howmany
   # print(random))