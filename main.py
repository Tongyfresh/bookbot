def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    letter_counts = get_count_letters(text)
    letter_counts_list = list(letter_counts.items())
    letter_counts_list.sort(key=lambda item: item[1], reverse=True)
    for letter, count in letter_counts_list:
        print(f"The {letter} character was found {count} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_letters(text):
    letters = {}
    for c in text:
        if c.isalpha():
            lowercase = c.lower()
            if lowercase in letters:
                letters[lowercase] += 1
            else:
                letters[lowercase] = 1
    return letters
    

main()