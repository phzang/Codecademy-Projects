class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User {name} email has been updated to {email}".format( \
            name = self.name, email = self.email))

    def __repr__(self):
        pass

    def __eq__(self, other_user):
        pass

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = [] 

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title} ISBN has been updated to {isbn}.".format( \
            title = self.title,
            isbn = self.isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        print("Invalid Rating")

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super.__init__(title, isbn)
        self.author = author

    def get_author(author):
        return self.author

    def __repr(self):
        pass
