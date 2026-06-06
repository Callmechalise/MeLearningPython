class Book:
    def  __init__(self, title, author,year):
        self.title=title
        self.author=author
        self.year=year
    def book_info(self):
        print(f'Title : {self.title} Author : {self.author} Published year : {self.year} ')

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f'{book} added')
    def show_books(self):
        if not self.books:
            print('No books in the library')
        for book in self.books:
            print(book)

def main():
    library=Library()

    while True:
        print('---Menu---')
        print('1:Add Book')
        print('2:Show Book')
        print('3:Exit')

        choice=input('Enter choice(1,2,3):\n')

        if choice=='1':
            title=input('Enter title of the book:\n')
            author=input('Enter author of the book:\n')
            year=input('Enter published year of the book:\n')
            x=Book(title,author,year)
            library.add_book(x)
        
        if choice=='2':
            library.show_books()

        if choice=='3':
            break

if __name__=='__main__':
    main()