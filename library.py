class user:
    def __init__(self, id, full_name, age, id_no):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no


class clint(user):
    def __init__(self, id, full_name, age, id_no, phone_number):
        self.phone_number = phone_number
        user.__init__(self, id, full_name, age, id_no)


class librarian(user):
    def __init__(self, id, full_name, age, id_no, employment_type):
        self.employment_type = employment_type
        user.__init__(self, id, full_name, age, id_no)


class book:
    def __init__(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status


class borrowing_order:
    def __init__(self, id, date, end_date, clint_id, book_id, status):
        self.id = id
        self.date = date
        self.clint_id = clint_id
        self.book_id = book_id
        self.status = status
        self.end_date = end_date


#########################################


list_of_librarians = []

c = clint(100, "mohand", 20, 33, 8768672)
c2 = clint(10, "hadeel", 26, 44, 876662)
c3 = clint(1000, "amal", 24, 55, 8766672)
l = librarian(245, "ismail", 19, 2092784, "full")
b1 = book(22, "English", "jjj", "gg", "active")
b2 = book(77, "arabic", "hh", "gug", "active")
b3 = book(99, "art", "jlj", "gjg", "active")
list_of_librarians.append(l)
list_of_books = [b1, b2, b3]
list_of_clients = [c, c2, c3]
o = borrowing_order(33, "4/5/2023", "3/3/2023", 3334, 7778, "active")


re_request = int(input("Enter the  id of book which want to borrow: "))

is_exist = False
for n in list_of_books:
    # print(n.id)
    if re_request in [99, 22, 77]:
        is_exist = True
        break
        print("true")
if not is_exist:
    print("the book is not exist")
d = int(input("enter user id: "))
is_exist = False
for n in list_of_clients:
    # print(n.id)
    if d in [10, 100, 1000]:
        is_exist = True
        print("true")
        break
    else:
        is_exist = False

if not is_exist:
    print("the user is not exist")

id_num = int(input("enter id no:"))
if id_num in [33, 44, 55]:
    print("true")
else:
    print("false id no")

len(list_of_clients)
len(list_of_books)

# class main_file:
#     client = ["Hadeel", "Ali", "Mona"]
#     client.append("Ismail")
#     client.clear()
#
#     print(client)
#
#
# for i in range(10, 15, 1):
#     print(i, end=",\n")
#
#     librarian = ["Adel", "Mohamed", "Waleed", "Malak", "Abdalla"]
#     librarian.append("Osama")
#     print(librarian)
#
#     book = []
#     for i in ["Pistachio theory", "English", "Art", "Diary", "philosophy"]:
#         book.append({"book": i, "status": "active", '7': "jj"})
#         book.append({"English": "inactive"})
#         book.append({"Art": "inactive"})
#     print(book)
#
#     re_request = str(input("Enter the book which want to borrow: "))
#
#     success = False
#     for i in book:
#         if i["status"] == re_request:
#             if i["status"] == "active":
#                 success = False
#             else:
#                 i["status"] = "active"
#                 success = True
#
#     if success:
#         print('\n your book reserved successfully')
#     else:
#         print('\n failed to reserve book')
