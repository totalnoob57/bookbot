def word_count(book):
    words=book.split()
    return len(words)

def letter_count(book):
    letters={}
    for char in book:
        if char.isalpha():
            char=char.lower()
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters