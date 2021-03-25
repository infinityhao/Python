# An object is instance of a particular type
# A class or type's methods are functions that every instance of that class or type provides.

# Import the library
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

class Circle(object):
    def __init__(self, radius = 3, color = "blue"): # constructor with double underscore on both sides
        self.radius = radius
        self.color = color
    # Method
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
        plt.axis("scaled")
        plt.show()

# Create object using object constructor
redCircle = Circle(10, "red")

# Find out the method can be used on this object
print("dir: ", dir(redCircle))

# print the radius
print("Print redCircle.radius: ", redCircle.radius) 

# print the color
print("Print redCircle.color: ", redCircle.color) 

# Set the object attribute radius
redCircle.radius = 1
print("Set the object attribute radius: ", redCircle.radius) 

# Use method to increase onject attribute radius
print("redCircle.add_radius(10): ", redCircle.add_radius(10))

# Call the method drawCircle
redCircle.drawCircle()

# Create a new object
blueCircle = Circle(radius = 100)
blueCircle.drawCircle()

# Import the library
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

#
class Rectangle(object):
    def __init__(self,height,width,color): 
        self.height = height
        self.width = width
        self.color = color

        # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.height, self.width, fc=self.color)) 
        plt.axis("scaled")
        plt.show()

# Create a new object
skinnyBlueRectangle = Rectangle(2 , 10, "blue")

# print the height
print("Print skinnyBlueRectangle.height: ", skinnyBlueRectangle.height) 

# print the width
print("Print skinnyBlueRectangle.width: ", skinnyBlueRectangle.width)

# print the color
print("Print skinnyBlueRectangle.color: ", skinnyBlueRectangle.color) 

# Call the method drawRectangle
skinnyBlueRectangle.drawRectangle()