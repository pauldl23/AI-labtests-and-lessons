# --- Encryption / Decryption ---
def encrypt_message(msg):
    step1 = [ln.split() for ln in msg.split('\n')]
    print("Step 1:", step1)

    step2 = [list(reversed(ln)) for ln in step1]
    print("Step 2:", step2)

    step3 = [[w[::-1] for w in ln] for ln in step2]
    print("Step 3:", step3)

    enc_msg = "\n".join(" ".join(ln) for ln in step3)
    print("Step 4:", enc_msg)
    return enc_msg


def decrypt_message(msg):
    step1 = [ln.split() for ln in msg.split('\n')]
    print("Step 1:", step1)

    step2 = [[w[::-1] for w in ln] for ln in step1]
    print("Step 2:", step2)

    step3 = [list(reversed(ln)) for ln in step2]
    print("Step 3:", step3)

    dec_msg = "\n".join(" ".join(ln) for ln in step3)
    print("\nDecrypted:", dec_msg)
    return dec_msg


# --- Input Helper ---
def get_input(msg="Enter text (end with ';'):"):
    print(msg)
    lines = []
    while True:
        ln = input()
        if ln.strip() == ";":
            break
        lines.append(ln)
    return "\n".join(lines)


# Encrypt
msg = get_input("Enter text to encrypt (end with ';'):")
encrypted = encrypt_message(msg)

print("\n Decryption")
print("-----------------------")

# Decrypt
enc_in = get_input("Enter text to decrypt (end with ';'):")
decrypt_message(enc_in)
