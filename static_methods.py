#Static Methods
#The given code takes 2 numbers as input and calls the static area() method of the Shape class, to output the area of the shape, which is equal to the height multiplied by the width.
#To make the code work, you need to define the Shape class, and the static area() method, which should return the multiplication of its two arguments.

#Use the @staticmethod decorator to define a static method.

#your code goes here
class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @staticmethod
    def area(w,h):
        return w *h


w = int(input("Enter the width:\n "))
h = int(input("Enter the height: \n"))

print(Shape.area(w, h))
