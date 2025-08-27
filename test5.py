# Input message (multiline until ';' is entered)
print("Enter your message (end with ';' on a new line):")
lines = []
while True:
    line = input()
    if line.strip() == ";":
        break
    lines.append(line)
msg = "\n".join(lines)

print("\nMsg:")
print(msg)

# Step1: split
s1 = [ln.split() for ln in msg.split("\n")]
print("\nS1:")
print(s1)

# Step2: rev words
s2 = [ln[::-1] for ln in s1]
print("\nS2:")
print(s2)

# Step3: rev chars
s3 = []
for ln in s2:
    s3.append([w[::-1] for w in ln])
print("\nS3:")
print(s3)

# Step4: flat
s4 = [" ".join(ln) for ln in s3]
enc = "\n".join(s4)

print("\nS4 (Enc):")
print(enc)


# Dec (reverse process)

print("\nDec:")

# D1
d1 = [ln.split() for ln in enc.split("\n")]
print("\nD1:")
print(d1)

# D2
d2 = [ln[::-1] for ln in d1]
print("\nD2:")
print(d2)

# D3
d3 = []
for ln in d2:
    d3.append([w[::-1] for w in ln])
print("\nD3:")
print(d3)

# D4
d4 = [" ".join(ln) for ln in d3]
dec = "\n".join(d4)

print("\nD4 (Dec):")
print(dec)
