def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return (len(words))

def count_characters(string):
    characters = {}
    lowered_string = string.lower()

    for character in lowered_string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters

# def convert_dict(dict):
    return [{key: value} for key, value in dict.items()]

# def sort_on(dict):
    return dict["num"]

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    # list_dict = convert_dict(num_characters)

    print(f"{num_words} words in text! {num_characters} characters in text!")

main()