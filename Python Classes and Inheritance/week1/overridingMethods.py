class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)

class PaperBook(Book):
    def __init__(self, title, author, numPages):
        Book.__init__(self, title, author)
        self.numPages = numPages

class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size
        

class Library:
    def __init__(self):
        self.book = []
    def addBook(self, book):
        self.book.append(book)
    def getNumBook(self):
        return len(self.book)

myBook = EBook('The Odyssey', 'Homer', 2)
myPaperBook = PaperBook('The Odyssey', 'Homer', 500)

print(myBook)
print(myPaperBook)

addl = Library()
addl.addBook(myBook)
addl.addBook(myPaperBook)

print(addl.getNumBook())
