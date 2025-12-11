def count_words(path):
    with open(path) as file:
        contents = file.read()
        words = []
        words = contents.split()
        print(f"Found {len(words)} total words")

def count_chars(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char not in chars:
            chars[char] = 0
        for letter in chars:
            if char == letter:
                chars[letter] += 1
    #print(chars)
    return chars

def get_char_key(char):
    return char["num"]

def report(unsorted_chars, book_path):
    sorted = []
    for char in unsorted_chars:
        if not char.isalpha():
            continue
        char_dict = {"char": f"{char}", "num": unsorted_chars[char]}
        sorted.append(char_dict)
    sorted.sort(key=get_char_key,reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    count_words(book_path)
    print("--------- Character Count -------")
    for char in sorted:
        letter = char["char"]
        count = char["num"]
        print(f"{letter}: {count}")