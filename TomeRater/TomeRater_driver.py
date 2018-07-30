#Driver to test TomeRater classes

import TomeRater as TR

s = TR.User("bob","bobemail")
print(s)

s.change_email("NewEmail")
print(s)

b = TR.User("joe", "nomail")

q = TR.User("Joe", "nomail")

print(q==b)

print("average rating " + str(q.get_average_rating()))

print("==============================")

book1 = TR.Book("Return of King", "2342523")
print(book1.get_title())
print(book1.get_isbn())
book1.set_isbn("11111111")
book1.add_rating(5)

book2 = TR.Book("Sup", "623532")
book3 = TR.Book("Sup", "623532")

print(book2 == book3)

print("=============================")

fict1 = TR.Fiction("Random Fiction", "Murdoc", "123145")
print(fict1)
print(fict1.get_author())

print("===============================")
non1 = TR.Non_Fiction("Random NonFiction", "bob", "intermediate","23434")
print(non1.get_subject())
print(non1.get_level())
print(non1)


ratings = []
if ratings:
    print("sup")
else:
    print("nope")
print(ratings)

print("===========================")
print("Book TEST")
book12 = TR.Book("Hunt for Red October", "ASDF@#$#@$)(@$")
book54 = TR.Book("Lord of the Flies", "908SDFSD")
print(book12.get_average_rating())
book12.add_rating(12) #should print "Invalid Rating"
book12.add_rating(3)
print(book12.get_average_rating())
book12.add_rating(1.72)
print(book12.get_average_rating())
print("====================")
print("TomeRater TEST")
tome1 = TR.TomeRater()
tome1.create_book("bob", "234234dfs")
tome1.add_book_to_user("bob", "joe@email.com")
tome1.add_user("Joe","joe@email.com")
tome1.add_book_to_user("bob", "joe@email.com")
tome1.print_catalog()
tome1.print_users()
