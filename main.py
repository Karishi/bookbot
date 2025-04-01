from stats import get_num_words, count_characters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    address = sys.argv[1]
    manuscript = get_book_text(address)
    print(f"Analyzing book found at {address}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(manuscript)} total words")
    print("--------- Character Count -------")
    letter_dict = count_characters(manuscript)
    for letter in sort_dict(letter_dict):
        print(f"{letter["character"]}: {letter["count"]}")
    print("============= END ===============")

main()