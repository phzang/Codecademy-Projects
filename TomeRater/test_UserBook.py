from TomeRater import *

name = "Bob"
email = "bob@bob.com"
books = {} #key:book, value: rating

test_user = User("Bob","bob@bob.com")

def test_init():
    assert test_user.name == name
    assert test_user.email == email

def test_email():
    assert test_user.get_email() == email

def test_change_email():
    address = "bob_newaddress@bob.com"
    test_user.change_email(address)
    assert test_user.get_email() == address


book1 = Book("Lord of the Flies", "ISBN234")
book2 = Book("Lord of the Flies", "ISBN234NEW")
book3 = Book("Lord of the Rings", "ISBN1234")
book4 = Book("Lord of the Randoms", "ISBN1234NEW")

book5 = Book("Lord of", 1215675345)
book6 = Book("Lord of", 1215675345)

def test_read_book():
    test_user.read_book(book1)
    assert test_user.books[book1] == None
    test_user.read_book(book2,5)
    test_user.read_book(book3,2)
    test_user.read_book(book4,4)
    assert round(test_user.get_average_rating(),2) == 3.67

def test_b_get_title():
    assert book1.get_title() == "Lord of the Flies"

def test_b_get_isbn():
    assert book1.get_isbn() == "ISBN234"

def test_b_set_isbn():
    book1.set_isbn("ISBN234NEW")
    assert book1.get_isbn() == "ISBN234NEW"

def test_b_add_rating():
    rating = 3
    book1.add_rating(rating)
    assert book1.ratings[0] == rating

def test_b_get_average_rating():
    book2.add_rating(2)
    book2.add_rating(1)
    book2.add_rating(-2)
    book2.add_rating(-10)
    book2.add_rating(4)
    book2.add_rating(6)
    book2.add_rating(None)

    assert round(book2.get_average_rating(),2) == 2.33

def test_b_eq():
    assert book1 == book2

def test_b_eq2():
    assert book5 == book6
