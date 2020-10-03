class Library:

    def __init__(self, listOfBooks, issuedBooks):
        self.listOfBooks = listOfBooks
        self.issuedBooks = issuedBooks

    def availableBooks(self):
        print("\nAvailable books in the Library :")
        for index, book in enumerate(self.listOfBooks, 1):
            print(f"{index}. {book}")

    def booksIssued(self):
        print("\nBorrowed books from the Library :")
        if(len(self.issuedBooks) >= 1):
            for stud, book in self.issuedBooks.items():
                print(f"{stud} has borrowed {book}")
        else:
            print("No books issued yet!!")

class Student:

    def borrowBook(self, studName, bookName):
        if bookName in listOfBooks:
            print(f"You borrowed {bookName}")
            listOfBooks.remove(bookName)
            if studName not in issuedBooks.keys():
                issuedBooks.update({studName:{bookName}})
            else:
                issuedBooks[studName].add(bookName)
        elif(bookName in issuedBooks.values()):
            print("Sorry!! This book has been issued by someone else")
        else:
            print("Sorry!! This book isn't available right now")

    def returnBook(self, studName, bookName):
        if studName in issuedBooks.keys():
            print("Book Returned, Thank You!!")
            listOfBooks.append(bookName)
            if len(issuedBooks[studName]) == 1:
                issuedBooks.pop(studName)
            else:
                issuedBooks[studName].remove(bookName)
        else:
            print("You haven't issued any book to return")

if __name__ == '__main__':
    listOfBooks = ["Python", "Machine Learning", "DSA", "Computer Networks", "Django", "Web Developement"]
    issuedBooks = dict()
    CentralLibray = Library(listOfBooks, issuedBooks)
    student = Student()

    print('''**********Welcome to Central Library***********\n
Please choose an available option
1. Display Avaialble Books
2. Display Borrowed Books
3. Borrow a Book
4. Return a Book
Press 'q' to quit''')

    while True:
        user_inp = input("\nEnter the option number : ")
        if(user_inp == '1'):
            CentralLibray.availableBooks()
        elif(user_inp == '2'):
            CentralLibray.booksIssued()
        elif(user_inp == '3'):
            studName = input("Enter your name\n").capitalize()
            bookName = input("Enter the name of book you want to borrow\n").casefold().title()
            student.borrowBook(studName, bookName)
        elif(user_inp == '4'):
            studName = input("Enter your name\n").capitalize()
            bookName = input("Enter the name of book you want to return\n").casefold().title()
            student.returnBook(studName, bookName)
        elif(user_inp == 'q' or user_inp == 'Q'):
            break
        else:
            print("Invalid Choice")

