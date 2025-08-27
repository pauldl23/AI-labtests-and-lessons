def get(*args, **kwargs):
    lines = []
    while True:
        line = input()
        if line.strip() == ";":
            break
        lines.append(line)
    return " ".join(lines)

# --- Analysis function ---
def anal(text, *args, **kwargs):
    words = []
    current = ""
    for ch in text:
        if ch.isalpha() or ch.isdigit():
            current += ch
        else:
            if current:
                words.append(current)
                current = ""
    if current:
        words.append(current)

    # reports
    print("\n--- Text Analysis Report ---")
    print("Total words:", len(words))
    print("Unique words:", len(set(words)))

    long_words = [w for w in words if len(w) > 5]
    print("Words longer than 5 characters:", long_words)

    caps = [w for w in words if w.isupper() and len(w) > 1]
    print("Capitalized words:", caps)

    return words

# --- Search function (loop inside) ---
def find(words, *args, **kwargs):
    while True:
        word = input("\nEnter word to search (or ';' to stop): ")
        if word.strip() == ";":
            break

        ignore = input("Ignore case? (yes/no): ").lower() == "yes"

        if ignore:
            count = sum(1 for w in words if w.lower() == word.lower())
        else:
            count = words.count(word)

        if count == 0:
            print("Word not found")
        else:
            print(f"'{word}' found {count} times")

# --- Main program ---
print("Enter text (end with ';' on a new line):")
text = get()
words = anal(text)
find(words)
print("Done.")
