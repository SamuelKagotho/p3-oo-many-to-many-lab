class Book:
    all_books = []  

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        self.title = title
        Book.all_books.append(self) 

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})

    def __str__(self):
        return f"Book Title: {self.title}"


class Author:
    all_authors = []  

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self.name = name
        Author.all_authors.append(self)  

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __str__(self):
        return f"Author Name: {self.name}"


class Contract:
    all = []  

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class")
        if not isinstance(date, str) or not date.strip():
            raise ValueError("Date must be a non-empty string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self) 

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __str__(self):
        return (
            f"Contract Details:\n"
            f"Author: {self.author.name}\n"
            f"Book: {self.book.title}\n"
            f"Date: {self.date}\n"
            f"Royalties: {self.royalties}"
        )
