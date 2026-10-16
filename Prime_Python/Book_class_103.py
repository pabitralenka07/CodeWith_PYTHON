class Book:
    def __init__(self,Title,Author):
        self.Title = Title
        self.Author = Author
        self.reviews = []

    def add_review(self,text):
        self.reviews.append(text)
    
    def count_reviews(self):
        return len(self.reviews)
    
    def display_all_reviews(self):
        print(self.reviews)

my_book = Book("DBE","RDBMS")

my_book.add_review("Cloud")
my_book.add_review("Data Science")
print(my_book.count_reviews())
my_book.display_all_reviews()
