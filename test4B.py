args = ()
kwargs = {}


get_input = lambda *args, **kwargs: " ".join(
    iter(
        lambda: (line := input()) if line.strip() != ";" else (_ for _ in ()).throw(StopIteration),
        None
    )
)

analyze_text = lambda text, *args, **kwargs: (
    # inside tuple to allow printing & returning awords
    (lambda words: (
        print("\n--- Text Analysis Report ---"),
        print("Total words:", len(words)),
        print("Unique words:", len(set(words))),
        print("Words longer than 5 characters:", list(filter(lambda w: len(w) > 5, words))),
        print("Capitalized words:", list(filter(lambda w: w.isupper() and len(w) > 1, map(lambda x: x.strip(), words)))),
        words
    )[-1])(  
        "".join(ch if (ch.isalpha() or ch.isdigit()) else " " for ch in text).split()
    )
)

search_word = lambda words, *args, **kwargs: (
    (lambda word_to_search, ignore_case: (
        print(
            f"Word '{word_to_search}' appears {sum(map(lambda w: (w.lower() if ignore_case else w) == (word_to_search.lower() if ignore_case else word_to_search), words))} time(s)."
        )
    ))(input("Enter special word to search: "), input("Ignore case while searching? (yes/no): ").lower() == 'yes')
)

main = lambda *args, **kwargs: (
    (lambda: [
        (lambda text, words: [
            search_word(words),
            None
        ])(get_input(), analyze_text(get_input()))  # calls twice for demonstration
        for _ in iter(lambda: input("Search again? (y/n): ").lower() == 'y', False)
    ])()
)

if __name__ == "__main__":
    while True:
        text = get_input()
        words = analyze_text(text)
        search_word(words)
        again = input("Search again? (y/n): ").lower()
        if again != 'y':
            break