class book:
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    
    def read(self):
        print(self.title,self.author,self.pages)

    def length(self):
        if self.pages > 200:
            print("the book",self.title,"is long")

book1 = book("hello","yuval",300)
book2 = book("banna","tal",150)
book3 = book("water","amit",120)

book_dict = {
    "book1": book1,
    "book2": book2,
    "book3": book3
}
choose = input("choose book")

if choose in book_dict:
    selected_book = book_dict[choose]
    selected_book.length()
    selected_book.read()
else:
    print("Invalid choice.")


