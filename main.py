import sys

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find the book at {path}.")
        sys.exit(1)
def main():
    file_contents=get_book_text(sys.argv[1])
    from stats import get_num_words
    from stats import get_num_character
    num_words = get_num_words(file_contents)
    num_character = get_num_character(file_contents)
    print(f'============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...')
    print(f'----------- Word Count ----------\n Found {num_words} total words')
    print(f'--------- Character Count -------')
    for item in num_character:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print(f'============= END ===============')

    
if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)