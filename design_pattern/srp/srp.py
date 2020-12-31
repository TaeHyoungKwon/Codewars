class Bookshelf:
    def __init__(self):
        self.books = []

    def add(self, name):
        self.books.append(name)

    def remove(self, name):
        return self.books.remove(name)

    def all_list(self):
        return '\n'.join(f"{index}: {book}" for index, book in enumerate(self.books, 1))

    # SRP를 위반 하는 메소드
    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.all_list())
