class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.books_list = []
        Author.members.append(self)

    def contracts(self):
        return self.contracts_list

    def books(self):
        return self.books_list

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The 'book' parameter must be an instance of the Book class.")
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        book.contracts_list.append(contract)  # Add contract to book's contracts_list
        book.authors().append(self)  # Add author to book's authors list
        self.books_list.append(book)  # Add book to author's books list
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)


class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.contracts_list = []  # Initialize an empty list to store contracts
        Book.members.append(self)

    def contracts(self):
        return self.contracts_list

    def authors(self):
        return [contract.author for contract in self.contracts_list]




class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The 'author' parameter must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The 'book' parameter must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The 'date' parameter must be of type string.")
        if not isinstance(royalties, int):
            raise Exception("The 'royalties' parameter must be of type int.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted(cls.members, key=lambda x: x.date)


if __name__ == "__main__":
    # Create authors
    author1 = Author("Author One")
    author2 = Author("Author Two")

    # Create books
    book1 = Book("Book One")
    book2 = Book("Book Two")

    # Sign contracts
    contract1 = author1.sign_contract(book1, "2024-03-10", 10)
    contract2 = author1.sign_contract(book2, "2024-03-11", 15)
    contract3 = author2.sign_contract(book1, "2024-03-10", 12)

    # Get contracts by date
    contracts_sorted = Contract.contracts_by_date("2024-03-10")

    print("Total royalties for Author One:", author1.total_royalties())
    print("Contracts sorted by date:", [contract.date for contract in contracts_sorted])
