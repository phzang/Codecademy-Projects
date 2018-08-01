from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

def test_add_user():
    assert Tome_Rater.users["alan@turing.com"] == User("Alan Turing", "alan@turing.com")
    assert Tome_Rater.users["david@computation.org"] == User("David Marr", "david@computation.org")
    #assert len(Tome_Rater.users) == 2

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

def test_add_user2():
    assert Tome_Rater.users["marvin@mit.edu"] == User("Marvin Minsky", "marvin@mit.edu")
    #assert len(Tome_Rater.users) == 3
    #assert len(Tome_Rater.users["marvin@mit.edu"].books) == 3
    #assert Tome_Rater.users["marvin@mit.edu"].books[0] == book1

def test_get_average_rating1():
    #assert print(Tome_Rater.users["marvin@mit.edu"].get_average_rating())
    pass

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


"""def test_add_book1():
    #assert print(Tome_Rater.users["alan@turing.com"])
    assert print(Tome_Rater.users["alan@turing.com"].books)"""

def test_get_average_rating2():
    assert Tome_Rater.users["alan@turing.com"].get_average_rating() == 2.4
