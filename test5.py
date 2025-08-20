
msg = """Hello, this is your
AI teacher, Sir iCE what
Do you want to do today"""

print("Msg:")
print(msg)

# Step1: split
s1 = [ln.split() for ln in msg.split("\n")]
print("\nS1:")
print(s1)

# Step2: rev words
s2 = []
for ln in s1:
    s2.append(ln[::-1])
print("\nS2:")
print(s2)

# Step3: rev chars
s3 = []
for ln in s2:
    nl = []
    for w in ln:
        nl.append(w[::-1])
    s3.append(nl)
print("\nS3:")
print(s3)

# Step4: flat
s4 = []
for ln in s3:
    s4.append(" ".join(ln))
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
d2 = []
for ln in d1:
    d2.append(ln[::-1])
print("\nD2:")
print(d2)

# D3
d3 = []
for ln in d2:
    nl = []
    for w in ln:
        nl.append(w[::-1])
    d3.append(nl)
print("\nD3:")
print(d3)

# D4
d4 = []
for ln in d3:
    d4.append(" ".join(ln))
dec = "\n".join(d4)

print("\nD4 (Dec):")
print(dec)
