# This part will let us use existing function for our objects.
# Example, I want the len of my class


mylist = [1,2,3]
print(len(mylist))

#class sample():
#    pass
#len(sample) # The result is this will fail with type error. 

# Here is an example
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 

    def __str__(self):
        return "{} by {}".format(self.title,self.author)

b = Book('Python rocks', 'Jose', 200)
print(b)