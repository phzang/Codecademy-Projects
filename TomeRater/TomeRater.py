class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}  # Book(object) : rating

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User {name}'s email has been updated to {email}".format(
            name=self.name, email=self.email))

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        books_with_ratings = 0
        for rating in self.books.values():
            if rating is not None:
                total_rating += rating
                books_with_ratings += 1
        if books_with_ratings:
            return total_rating / books_with_ratings
        return 0

    def get_number_of_books(self):
        return len(self.books)

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books_read}".format(
            user=self.name, email=self.email, books_read=len(self.books))

    def __eq__(self, other_user):
        return (self.name == other_user.name) and (self.email == other_user.email)

    def __hash__(self):
        return hash((self.name, self.email))


class Book(object):
    def __init__(self, title, isbn, price = None):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = None

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def get_average_rating(self):
        total_rating = 0
        valid_ratings = 0
        for r in self.ratings: 
            if r is not None:
                total_rating += r
                valid_ratings += 1
        if valid_ratings:
            return total_rating / valid_ratings
        return 0

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title} ISBN has been updated to {isbn}.".format(
            title=self.title,
            isbn=self.isbn))

    def set_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
            print("{title} price has been updated to {price}.".format(
                title=self.title,
                price=self.price))
        else:
            print("Please enter a valid price.")

    def add_rating(self, rating):
        # rating == None prevents TypeError >= 'NoneType' and 'int'
        if (rating is None) or (0 <= rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_user):
        return (self.title == other_user.title) and (self.isbn == other_user.isbn)

    def __repr__(self):
        return "{title}".format(
            title=self.title)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(
            title=self.title,
            author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject  # string
        self.level = level  # string

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(
            title=self.title, level=self.level, subject=self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}  # email : User(object)
        self.books = {}  # Book(object) : number of Users that have read it
        self.library = {}  # ISBN : Book(objects) that were created

    def isbn_exists(self, isbn):
        if isbn in self.library:
            return True
        return False

    def create_book(self, title, isbn):
        if self.isbn_exists(isbn):
            print("ISBN #{isbn} already exists!".format(isbn=isbn))
            return False
        self.library[isbn] = Book(title, isbn)
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        if self.isbn_exists(isbn):
            print("ISBN #{isbn} already exists!".format(isbn=isbn))
            return False
        self.library[isbn] = Fiction(title, author, isbn)
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        if self.isbn_exists(isbn):
            print("ISBN #{isbn} already exists!".format(isbn=isbn))
            return False
        self.library[isbn] = Non_Fiction(title, subject, level, isbn)
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

    def add_user(self, name, email, user_books=None):
        if self.valid_email(email):
            if email in self.users:
                print("User with email {email} already exists!".format(
                                                    email=email))
            else:
                self.users[email] = User(name, email)
                if user_books:
                    for b in user_books:
                        self.add_book_to_user(b, email)
            return True
        else:
            print("Please enter a valid email")
            return False

    def print_catalog(self):
        for book in self.books:
            print(book.get_title())

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        return max(self.books, key=self.books.get)

    def get_worth_of_user(self, user_email):
        total = 0
        if user_email in self.users:
            for book in self.users[user_email].books:
                if book.get_price() is not None:
                    total += book.get_price()
        return total

    def highest_rated_book(self):
        tmp_book = Book("", "")
        high_rating = 0
        for book in self.books:
            if book.get_average_rating() >= high_rating:
                tmp_book = book
                high_rating = book.get_average_rating()
        return tmp_book

    def most_positive_user(self):
        tmp_user = User("", "")
        high_rating = 0
        for user in self.users.values():
            if user.get_average_rating() >= high_rating:
                tmp_user = user
                high_rating = user.get_average_rating()
        return tmp_user
        
    def valid_email(self, email):
        try:
            if email.find("@"):
                email_split = email.split('@')                    
                email_dot_split = str(email_split[1]).split('.')
            
                if (email_dot_split[1] == "com") or  \
                   (email_dot_split[1] == "edu") or  \
                   (email_dot_split[1]) == "org":
                    return True
        
        except IndexError:
            return False
        return False

    def get_n_most_read_books(self, n):
        sorted_books = sorted(self.books, key=self.books.get, reverse=True)
        # prevent Index out of range error
        if n > len(sorted_books):
            n = len(sorted_books)
        tmp = []
        for b in range(0, n):
            tmp.append(sorted_books[b])
        return tmp

    def get_n_most_expensive_books(self, n):
        tester = {}
        for book in self.books:
            tester[book] = book.get_price()
            
        sorted_readers = sorted(tester, key=tester.get, reverse=True)
        # prevent Index out of range error
        if n > len(sorted_readers):
            n = len(sorted_readers)

        tmp = []
        for b in range(0, n):
            tmp.append(sorted_readers[b])
        return tmp
        
    def __repr__(self):
        total = 0
        for book in self.books:
            if book.get_price() is not None:
                total += book.get_price()
        return "Tome Rater has {users} users, {books} books, worth ${total}".format(
                users=len(self.users), books=len(self.books), total=total)
                 
    def __eq__(self, other):
        return ((self.users == other.users) and
                (self.books == other.books) and
                (self.library == other.library))    
