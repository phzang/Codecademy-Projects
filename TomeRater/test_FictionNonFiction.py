from TomeRater import *

name = "Bob"
email = "bob@bob.com"
books = {} #key:book, value: rating

test_user = User("Bob","bob@bob.com")




book1 = Fiction("Lord of the Flies","Fiction Author", "ISBN234")
book2 = Fiction("Lord of the Rings", "New Fiction Aurthor", "ISBN234NEW")
book3 = Non_Fiction("Lord of the Non", \
                    "Random Subject", "Advanced", "ISBNnon234")
book4 = Non_Fiction("Lord of the NonFiction", \
                    "Another Random Subject", "Novice", "ISBNnon234NEW")

def test_f_get_author():
    assert book1.get_author() == "Fiction Author"
    assert book2.get_author() == "New Fiction Aurthor"
    
def test_nf_get_subject():
    assert book3.get_subject() == "Random Subject"
    assert book4.get_subject() == "Another Random Subject"

def test_nf_get_level():
    assert book3.get_level() == "Advanced"
    assert book4.get_level() == "Novice"
