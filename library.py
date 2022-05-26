class clint:
    def __init__(self, id, full_name, age, id_no, phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number


class librarian(clint):
    def __init__(self, emplyment_type):
        self.emplyment_type = emplyment_type
        obj = clint(33, 'ismail', 80, 837, 92865345)


class book:
    def __init__(self, id, title, description, author, status):
        self.id = id
        self.titil = title
        self.description = description
        self.author = author
        self.status = status


class borrowing_order:
    def __init__(self, id, data, clint_id, book_id, status):
        self.id = id
        self.data = data
        self.clint_id = clint_id
        self.book_id = book_id
        self.status = status


#########################################
c = clint(100, "hadeel", 20, 3333, 8768672)
l=librarian(245)

class main_file:
    client = ["Hadeel", "Ali", "Mona"]
    client.append("Ismail")
    print(client)

    librarian = ["Adel", "Mohamed", "Waleed", "Malak", "Abdalla"]
    librarian.append("Osama")
    print(librarian)

    book = []
    for i in ["Pistachio theory", "English", "Art", "Diary", "philosophy"]:
        book.append({"book": i, "status": "active"})
        book.append({"English": "inactive"})
        book.append({"Art": "inactive"})
    print(book)

    re_request = str(input("Enter the book which want to borrow: "))

    success = False
    for i in book:
        if i["status"] == re_request:
            if i["status"] == "active":
                success = False
            else:
                i["status"] = "active"
                success = True

    if success:
        print('\n your book reserved successfully')
    else:
        print('\n failed to reserve book')
