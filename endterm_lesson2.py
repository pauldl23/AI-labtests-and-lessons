char_set = set('hello')
print(type(char_set), char_set)

squares = {x * x for x in range(5)}
print(type(squares), squares)


generator_exp = (x for x in range(5))
print(type(generator_exp), generator_exp)



#ways to copy values for set
original = {1,2,3}
copyset = set(original)
print(type(copyset), copyset)