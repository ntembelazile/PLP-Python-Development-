# Base class Book
class Book:
    def __init__(self, title, author, genre, publication_year, price):
        self.title = title            # Public attribute
        self.author = author          # Public attribute
        self._genre = genre           # Protected attribute
        self.__publication_year = publication_year  # Private attribute
        self.__price = price          # Private attribute

    # Getter method for private attributes
    def get_price(self):
        return self.__price

    def get_publication_year(self):
        return self.__publication_year

    # Setter method for price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price cannot be zero or negative.")
    
    # A method to describe the book
    def describe_book(self):
        return f"'{self.title}' by {self.author}, Genre: {self._genre}, Published: {self.__publication_year}, Price: ${self.__price}"

# Derived class FictionBook (Inheritance)
class FictionBook(Book):
    def __init__(self, title, author, publication_year, price, sub_genre, series=None):
        super().__init__(title, author, "Fiction", publication_year, price)
        self.sub_genre = sub_genre
        self.series = series

    def describe_book(self):
        description = super().describe_book()
        if self.series:
            description += f", Series: {self.series}"
        description += f", Sub-genre: {self.sub_genre}"
        return description

# Derived class NonFictionBook (Inheritance)
class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, price, topic):
        super().__init__(title, author, "Non-Fiction", publication_year, price)
        self.topic = topic

    def describe_book(self):
        description = super().describe_book()
        description += f", Topic: {self.topic}"
        return description

# Create instances of the Book, FictionBook, and NonFictionBook classes
book1 = Book("Generic Book", "Unknown Author", "Mystery", 2022, 19.99)
fiction_book1 = FictionBook("The Great Adventure", "John Doe", 2023, 25.99, "Fantasy", "The Fantasy Saga")
nonfiction_book1 = NonFictionBook("Science Explained", "Dr. Jane Smith", 2020, 30.00, "Physics")

# Test the methods
print(book1.describe_book())  # Basic book
print(fiction_book1.describe_book())  # Fiction book with series
print(nonfiction_book1.describe_book())  # Non-fiction book with topic

# Testing encapsulation with getters and setters
print(f"Original price of '{fiction_book1.title}': ${fiction_book1.get_price()}")
fiction_book1.set_price(29.99)  # Change price
print(f"Updated price of '{fiction_book1.title}': ${fiction_book1.get_price()}")

# Trying to set an invalid price
fiction_book1.set_price(-5)
