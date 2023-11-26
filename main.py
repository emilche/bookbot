def main():
    book = Book("frankenstein.txt")
    print(book.print_report())

class Book():
    def __init__(self, name):
        self.book_name = name
        self.path_to_book = f"books/{name}"
        self.book_content = self.load_book_content()

    def get_num_words(self) -> int:
        return len(self.book_content.split())

    def get_num_letters(self) -> dict:
        chars = {}
        for letter in self.book_content:
            if letter.lower() in chars:
                chars[letter.lower()] += 1
            else:
                chars[letter.lower()] = 1
        return chars

    def load_book_content(self) -> str:
        with open(self.path_to_book) as f:
            return f.read()
    
    def print_report(self):
        print(f"--- Begin report of {self.path_to_book} ---")
        print(f"{self.get_num_words()} words found in the document")
        letter_dict = self.get_num_letters()
        values = list(letter_dict.values())
        values.sort(reverse=True)
        for value in values:
            for key in letter_dict:
                if letter_dict[key] == value:
                    if not key.isalpha():
                        break
                    print(f"The '{key}' character was found {value} times")
                    break
        print("--- End report ---")
            



main()