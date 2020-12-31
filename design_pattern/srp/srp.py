class Bookshelf:
    def __init__(self):
        self.books = []

    def add(self, name):
        self.books.append(name)

    def remove(self, name):
        return self.books.remove(name)

    def all_list(self):
        return "\n".join(f"{index}: {book}" for index, book in enumerate(self.books, 1))


class BookshelfFileIO:
    @staticmethod
    def save_to_file(bookshelf, filename):
        with open(filename, "w") as file:
            file.write(bookshelf.all_list())

    @staticmethod
    def load_to_file(filename):
        with open(filename, "r") as file:
            return "".join(file.readlines())


if __name__ == "__main__":
    book_shelf = Bookshelf()
    book_shelf.add("refactoring")
    book_shelf.add("clean_code")
    book_shelf.add("clean_coder")

    io = BookshelfFileIO()
    io.save_to_file(book_shelf, "book_shelf.txt")
    print(io.load_to_file("book_shelf.txt"))
