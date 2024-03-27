import os


class book:

    books = 0

    def __init__(self, name, price, page):
        self.name = name
        self.price = price
        self.page = page

        book.books += 1

    def display(self):
        clear()
        print(f"Name  : {self.name}")
        print(f"Price : {self.price}")
        print(f"Pages : {self.page}")
        os.system("pause")

    def dis(self, discount):
        self.discount = discount
        self.price = self.price - self.price * self.discount

    @classmethod
    def add(cls):
        name = input("Name : ")
        try:
            price = int(input("Price : "))
        except ValueError:
            input("Enter Valid value only")
            add()
            return
        try:
            pages = int(input("Pages : "))
        except ValueError or TypeError:
            input("Enter Valid value only")
            add()
            return
        return cls(name, price, pages)


def clear():
    os.system("cls")


def pause():
    os.system("pause")


books = []
no = 0


def main():
    clear()
    print("1. Add book")
    print("2. Display Books")
    print("3. Book Info")
    print("4. Remove Book")
    print("5. Exit")
    try:
        inp = int(input("Choice : "))
    except ValueError:
        print("Enter Valid Value!!")
        return
    return inp


def add():
    clear()
    books.append(book.add())


def show():
    clear()
    try:
        if len(books) != 0:
            index = 1
            for i in books:
                if i is not None:
                    print(f"{index} . {i.name}")
                    index += 1
            input()
        else:
            input("\tNo book Found!!")
    except IndexError or AttributeError:
        return


def info():
    clear()
    if len(books) != 0:
        index = 1
        for i in books:
            if i is not None:
                print(f"{index} . {i.name}")
                index += 1
        try:
            ch = int(input("Which Book : "))
            ch -= 1
            try:
                books[ch].display()
            except IndexError:
                input('\nInValid Book!!')
                return
        except ValueError:
            input('\nInvalid book!!')
            return
    else:
        input("\nNo book Found!!")


def rem():
    try:
        if len(books) != 0:
            index = 1
            for i in books:
                if i is not None:
                    print(f"{index} . {i.name}")
                    index += 1
            ch = int(input("Which Book : "))
            ch -= 1
            del books[ch]
        else:
            input("\nNo book Found!!")
    except IndexError:
        return


while True:
    op = main()
    if op == 1:
        add()
    elif op == 2:
        show()
    elif op == 3:
        info()
    elif op == 4:
        rem()
    elif op == 5:
        exit()
    else:
        input("\tinvalid operation")
