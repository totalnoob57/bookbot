def get_book_text(file_path):
    with open(file_path) as file:
        book=file.read()
    file.close
    return book

from stats import word_count, letter_count

def main():
    book=get_book_text("books/frankenstein.txt")
    #word_count=count(book)
    letters = letter_count(book)
    print(letters)


main()