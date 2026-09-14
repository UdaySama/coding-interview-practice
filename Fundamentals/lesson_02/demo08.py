class Book:

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def get_description(self):
    return f"'{self.title}' written by {self.author}"


my_book = Book(title="1984", author="George Orwell")
print(my_book.get_description())