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
            print("Enter Valid value only")
            add()
            return
        try:
            pages = int(input("Pages : "))
        except ValueError or TypeError:
            print("Enter Valid value only")
            add()
            return
        return cls(name, price, pages)


def clear():
    os.system("cls")


def pause():
    os.system("pause")

books = []

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
    try:
        books.append(book.add())
    except UnboundLocalError or TypeError:
        return


def show():
    try:
        if len(books) != 0:
            index = 1
            for i in books:
                if i is not None:  
                    print(f'{index} . {i.name}' )
                    index += 1
            pause()
        else:
            print("No book Found!!")
            pause()
    except IndexError or AttributeError:
        return


def info():
    try:
        if len(books) != 0:
            index = 1
            for i in books:
                print(f"{index} . {i.name}")
                index += 1
            ch = int(input("Which Book : "))
            ch -= 1
            books[ch].display()
        else:
            print("No book Found!!")
            pause()
    except IndexError or ValueError:
        return


def rem():
    try:
        if len(books) != 0:
            index = 1
            for i in books:
                print(f"{index} . {i.name}")
                index += 1
            ch = int(input("Which Book : "))
            ch -= 1
            del books[ch]
        else:
            print("No book Found!!")
            pause()
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
        print("invalid operation")
