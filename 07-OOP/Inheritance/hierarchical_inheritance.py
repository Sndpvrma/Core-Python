#
# class Shape:
#     def __init__(self, color='', border_width=0):
#         self.color = color
#         self.border_width = border_width
#
#     def setcolor(self, c):
#         self.color = c
#
#     def getcolor(self):
#         return self.color
#
#     def setborder_width(self, bw):
#         self.border_width = bw
#
#     def getborder_width(self):
#         return self.border_width
#
# class Rectangle(Shape):
#     def __init__(self, length=0, width=0, color='', border_width= 0):
#         self.length = length
#         self.width = width
#         super().__init__(color, border_width)
#
#     def setlength(self, l):
#         self.length = l
#
#     def getlength(self):
#         return self.length
#
#     def setwidth(self, w):
#         self.width = w
#
#     def getwidth(self):
#         return self.width
#
# class Circle(Shape):
#     def __init__(self, radius = 0, color = '', border_width = 0):
#         self.radius = radius
#         super().__init__(color, border_width)
#
#     def setradius(self, r):
#         self.radius = r
#
#     def getradius(self):
#         return self.radius
#
# r=Rectangle(10, 20, 'green', 100)
# print("Rectangle:")
# print("Length:", r.getlength())
# print("Width:", r.getwidth())
# print("Color:", r.getcolor())
# print("Border_width:", r.getborder_width())
#
# c=Circle(15, 'yellow', 50)
# print("\ncircle:")
# print("Radius:", c.getradius())
# print("Color:", c.getcolor())
# print("Border_width:", c.getborder_width())

class Shape:
    def __init__(self, color = '', border_width = 0):
        self.color = color
        self.border_width = border_width

    def setcolor(self, c):
        self.color = c
    def getcolor(self):
        return self.color

    def setborder_width(self, bw):
        self.border_width = bw
    def getborder_width(self):
        return self.border_width

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0, color = '', border_width = 0):
        self.length = length
        self.width = width
        super().__init__(color, border_width)

    def setlength(self, l):
        self.length = l
    def getlength(self):
        return self.length

    def setwidth(self, w):
        self.width = w
    def getwidth(self):
        return self.width

class Circle(Shape):
    def __init__(self, radius = 0, color = '', border_width = 0):
        self.radius = radius
        super().__init__(color, border_width)

    def setradius(self, r):
        self.radius = r
    def getradius(self):
        return self.radius

r = Rectangle(50, 70, 'blue', 170)
print("\nRectangle:")
print("Length:", r.getlength())
print("width:", r.getwidth())
print("Color:", r.getcolor())
print("border_width:", r.getborder_width())

c=Circle(70, 'purple', 220)
print("\nCircle:")
print("Radius:", c.getradius())
print("Color:", c.getcolor())
print("Border_width:", c.getborder_width())