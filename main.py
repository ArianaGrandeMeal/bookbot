def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count_words(text)
    count_chars(text)
    print_report(text)
    
# open file path, return file contents as string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# split text string into words, return number of words 
def count_words(text):
    words = text.split()
    return len(words)

# iterate text file, converted to lowercase, to add new characters
# to chars dictionary and count characters already in dictionary
# returns dictionary of format [character: instances]
def count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def print_report(text):
    sorted_letter_count = []
    dict_list = list(count_chars(text).items())

    dict_list.sort(key=lambda a: a[1], reverse=True)
    
    for item in dict_list:
        if item[0].isalpha():
            sorted_letter_count.append(item)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document " '\n')
    for item in sorted_letter_count:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")
    
    

main()