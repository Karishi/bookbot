import random
from stats import get_num_words, count_characters, sort_dict, slice_by_word
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
    print("--------- Word Analysis ---------")
    word_dict = slice_by_word(manuscript)
    word_list = sort_dict(word_dict)
    out = False
    while not out:
        pick = input("Please input a word you want to know about. Type quit! to quit. > ")
        if pick.lower() == "quit!":
            out = True
        elif pick.lower() not in word_dict:
            print(f"\"{pick.lower()}\" doesn't appear in the book at {address}")
        else:
            print(f"\"{pick.lower()}\" appears {word_dict[pick.lower()]} times.")
            word_index = word_list.index(pick.lower())
            word_index_down = word_index
            word_index_up = word_index
            sublist = []
            while word_index_down > 0 and word_dict[word_list[word_index_down-1]] == word_dict[pick.lower()]:
                word_index_down -= 1
                sublist.append(word_dict[word_list[word_index_down]])
            while word_index_up < len(word_list) - 1 and word_dict[word_list[word_index_up + 1]] == word_dict[pick.lower()]:
                word_index_up += 1
                sublist.append(word_dict[word_list[word_index_up]])
            matching_word = random.choice(sublist)
            print(f"The word {matching_word} has the same number of appearances.")

    # print("--------- Character Count -------")
    # letter_dict = count_characters(manuscript)
    # for letter in sort_dict(letter_dict):
        # print(f"{letter["character"]}: {letter["count"]}")
    print("============= END ===============")

main()