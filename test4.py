def input():
    print('Enter your multiline text, type ; on a new line to finish: ')
    lines = []
    while True:
        line = input()
        if line.strip() == ';':
            break
        lines.append(line)
    return " ".join(lines)
    print(lines)

def analysis(text):
    unique= []
    for word in words:
            if word not in unique:
                unique.append(word)
    return len(unique)
    print(unique)
    
    
