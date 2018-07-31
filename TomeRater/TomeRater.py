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
        if self.books:    
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
            total_rating += r
        if self.ratings:
            return total_rating / len(self.ratings)
        return 0

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title} ISBN has been updated to {isbn}.".format( \
            title = self.title,
            isbn = self.isbn))

    def add_rating(self, rating):
        if rating != None and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
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

class Non_Fiction(Book):
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
        self.users = {} #email : User(object)
        self.books = {} #Book(object) : number of Users that have read it

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=None):        
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email=email))

    #needs work			
    def add_user(self, name, email, books=None):
        self.users[email] = User(name,email)
        if books:
            for b in books:
                self.add_book_to_user(b,email)

    def print_catalog(self):
        print("print_catalog()")
        for book in self.books:            
            print(book.get_title())

    def print_users(self):
        print("print_users()")
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        print(max(self.books,key=self.books.get))

    def highest_rated_book(self):
        tmp_book = Book("","")
        high_rating = 0
        for book in self.books:            
            if book.get_average_rating() >= high_rating:
                tmp_book = book
                high_rating = book.get_average_rating()
        return tmp_book
    
    #needs work
    def most_positive_user(self):
        tmp_user = User("","")
        high_rating = 0
        for user in self.users.values():
            if user.get_average_rating() >= high_rating:
                tmp_user = user
                high_rating = user.get_average_rating()
        return tmp_user
