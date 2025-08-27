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
    # tokenize: extract only alnum words
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

    
    long_words = list(filter(lambda w: len(w) > 5, words))
    print("Words longer than 5 characters:", long_words)

    
    caps = list(filter(lambda w: w.isupper() and len(w) > 1, words))
    print("Capitalized words:", caps)

   
    word_lengths = list(map(lambda w: (w, len(w)), words))
    print("Word lengths:", word_lengths)

    return words


# --- Search function ---
def find(words, *args, **kwargs):
    while True:
        word = input("\nEnter word to search (or ';' to stop): ")
        if word.strip() == ";":
            break

        ignore = input("Ignore case? (yes/no): ").lower() == "yes"

        # map + filter + lambda for counting
        if ignore:
            count = len(list(filter(lambda w: w.lower() == word.lower(), words)))
        else:
            count = len(list(filter(lambda w: w == word, words)))

        print(f"'{word}' found {count} times" if count > 0 else "Word not found")


# --- Main program ---
print("Enter text (end with ';' on a new line):")
text = get()
words = anal(text)
find(words)
print("Done.")
