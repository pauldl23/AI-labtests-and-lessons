text = input("Enter a string: ")
space = text.find(" ")
w1 = text[:space]
w2 = text[space+1:]
print("Output 1:", w2, w1)
print("Output 2:", w1[1:-1] + w2[1:-1])
print("Output 3:", w1[0] + w1[-1] + w2[0] + w2[-1])