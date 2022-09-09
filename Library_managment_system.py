class library:

    def __init__(self,books):
        self.book =books

    def displayavaliablebooks(self):
        print("The available books in the :")
        for book in self.book :
            print(" *",book)

    def barrowbook(self,bookname):
        if bookname in self.book:
            print(f"The Requested book {bookname} has been issued! , Please return it before 30 Days")
            self.book.remove(bookname)
            return True
        else:
            print(f"The Book You have requested has been issued to someone else Please wait until it is returned")
            return False

    def returnbook(self,bookname):
        self.book.append(bookname)
        print("Thanks for returning the book in time have a nice day:")



class student:
    def requestBook(self) :
        self.book = input("Enter the name of the book you want to borrow " )
        return self.book

    def returnbook(self):
        self.book = input("Enter the name of the book you want to return " )
        return self.book

if __name__ == "__main__" :
    centrallibrary =library(["gita","mahabhrath","visnu puran","garuda puran"])
    
    while(True):
        welcomemsg = '''====== Welcome to the central library ======
        1.list all the books
        2.Barrow a Book
        3.Add/return a book
        4.Exit the library
        '''
        students = student()
        print(welcomemsg)
        choices = int(input("Enter Your choice:"))
        if choices == 1:
            centrallibrary.displayavaliablebooks()
        elif choices == 2:
            centrallibrary.barrowbook(students.requestBook())
        elif choices == 3:
            centrallibrary.returnbook(students.returnbook())
        elif choices == 4:
            exit()
        else:
            print("Invalid choice")
