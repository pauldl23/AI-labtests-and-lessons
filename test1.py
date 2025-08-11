text = input("Enter a string: ") #sample text
words = text.split(' ')
print(words[1] + ' ' + words[0])
#print(text[7:] + ' '+text[0:7] )
print(text[1:6] + text[9])
print(text[0:6:5] + text[-1]*2)

print('---------------------------------')
word = input("Enter another string: ") #extremely humid
word2 = word.split(' ')
print(word2[1] + ' ' + word2[0])
#print(word[10:] + ' ' + word[0:9])
print(word[1:8] +  word[11:14])
print(word[0:9:8] + word[-5]+ word[-1])