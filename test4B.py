def get_input():
    print("Enter your multiline input (type ';' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == ';':
            break
        lines.append(line)
    return " ".join(lines)

def analyze_text(text):
    import re
    words = re.findall(r"\b\w+\b", text)  # extract words only
    total_words = len(words)
    unique_words = len(set(words))
    
    long_words = [word for word in words if len(word) > 5]
    
    capitalized_words = [word for word in words if len(word) > 1 and word[0].isupper() and word[-1].isupper()]
    
    print("\n--- Text Analysis Report ---")
    print("Total words:", total_words)
    print("Unique words:", unique_words)
    print("Words longer than 5 characters:", long_words)
    print("Capitalized words:", capitalized_words)
    
    return words

def search_word(words):
    word_to_search = input("Enter special word to search: ")
    ignore_case = input("Ignore case while searching? (yes/no): ").lower() == 'yes'
    
    count = 0
    if ignore_case:
        count = sum(1 for word in words if word.lower() == word_to_search.lower())
    else:
        count = words.count(word_to_search)
        
    print(f"Word '{word_to_search}' appears {count} time(s).")

def main():
    while True:
        text = get_input()
        words = analyze_text(text)
        search_word(words)
        again = input("Search again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()