class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} #key:book, value: rating

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User {name}'s email has been updated to {email}".format( \
            name = self.name, email = self.email))

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        for rating in self.books.values():
            total_rating += rating
        if len(self.books):    
            return total_rating / len(self.books)
        return 0       

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books_read}".format( \
            user = self.name, email = self.email, books_read = len(self.books))

    def __eq__(self, other_user):
        return (self.name == other_user.name) and (self.email == other_user.email)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_average_rating(self):
        total_rating = 0
        for r in self.ratings:
            r += total_rating
        if len(self.ratings):
            return total_rating / len(self.ratings)
        return 0

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title} ISBN has been updated to {isbn}.".format( \
            title = self.title,
            isbn = self.isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        print("Invalid Rating")    

    def __eq__(self, other_user):
        return (self.title == other_user.title) and (self.isbn == other_user.isbn)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format( \
            title = self.title,
            author = self.author)

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject #string
        self.level = level #string

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format( \
            title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if self.users.key == email:
            self.users.read_book(book, rating)
            book.add_rating(rating)
        

    
