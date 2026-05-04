class Libray:
  def __init__(self):
    self.nobook=0
    self.books=[]

def addBook(self,book):
  self.books.append(book)
  self.Nobooks=len(self.books)

def showInfo(self):
  print(f"The library has {self.nobook} books. The books are ")
  for book in self.book:
    print(book)
def lendBook(self,book):
  if book in self.books:
    print("You have been lent the book")
    self.books.remove(book)
  else:
    print("Sorry this book is not available")
def returnBook(self,book):
  self.books.append(book)
  print("You have returned the book")
myLibrary=Libray()


