import string


def normalize_word(word):
   return word.lower()


def text_analysis(*args, **kwargs):
   text = ' '.join(args)
   words = text.split()
   total_words = len(words)


   unique_words_set = set(map(normalize_word, words))
   unique_words = len(unique_words_set)


   long_words = list(filter(lambda w: len(w) > 5, words))


   capitalized_words = []
   for w in words:
       if len(w) >= 2:
           w = w[0].upper() + w[1:-1].lower() + w[-1].upper()
       capitalized_words.append(w)


   print("\n--- Text Analysis Report ---")
   print(f"Total words: {total_words}")
   print(f"Unique words: {unique_words}")
   print("\nWords longer than 5 characters:")
   print(long_words)
   print("\nCapitalized Words:")
   print(capitalized_words)


def count_special_word(words, special_word, ignore_case=True):
   if ignore_case:
       return sum(1 for w in words if normalize_word(w) == special_word.lower())
   else:
       return sum(1 for w in words if w == special_word)


while True:
   print("Enter your multiline input (type ';' on a new line to finish):")
   lines = []
   while True:
       line = input()
       if line.strip() == ';':
           break
       lines.append(line)
   text_input = "\n".join(lines)
   words_list = text_input.split()


   text_analysis(text_input)


   while True:
       special_word = input("\nEnter special word to search: ")
       ignore_case = input("Ignore case while searching? (y/n): ").strip().lower() == "y"
       count = count_special_word(words_list, special_word, ignore_case)
       print(f"\nWord '{special_word}' appears {count} time(s).")


       again = input("\nSearch again? (y/n): ").strip().lower()
       if again != 'y':
           break


   break
