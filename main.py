import sys
from stats import get_characters, get_word_count, book_report


def get_book_text(file) -> str:
    with open(file=file) as f:
        book: str = f.read()
        
    return book


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        book_text = get_book_text(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}")
        print("----------- Word Count ----------")
        print(f"Found {get_word_count(book_text=book_text)} total words")
        print("--------- Character Count -------")
        total_chars = book_report(book_characters=get_characters(book_text=book_text))
        for item in total_chars:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")
    
    
    
main()