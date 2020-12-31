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
