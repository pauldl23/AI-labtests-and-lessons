tup1=()
print(tup1)

#method2
tup2=(1,2,3,'apple','Banana')
print(tup2)

#method3
single_tuple=(1)
print(type(single_tuple))

#method4
tup3 = 11,12,23
print(type(tup3),tup3)

#method5
tup4 = tuple([1,2,3])
print(type(tup4),tup4)

tup5 = tuple('abc')
print(type(tup5),tup5)
single_tuple = tuple("1")

tup6=tuple(range(5,11))
print(type(tup6), tup6)

tup8 = (1,(2,3),(4,5))
print(type(tup8),tup8)
print(tup8[2][1])
print('+'*20)

    
for i, row in enumerate(tup8):
    print(f'ROW: {i} VALUE:{row}')
    if isinstance(row, (tuple, list)):
        for value in row:
            print(f'    value: {value}')
    else:
        print(f'    value: {row}')
    