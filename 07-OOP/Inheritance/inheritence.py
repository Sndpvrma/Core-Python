#Inheritence :- Jab ham kisi parent class/general ki properties child class/specilized me use
# karte hai to usko inheritence kehte hai, iska use specialization ke liye kiya jata hai.
# from first import colors


# class Shape:
#     def __init__(self):
#         self.color = " "
#         self.borderwidth = 0
#
#     def setcolor(self, c):
#         self.color = c
#
#     def getcolor(self):
#         return self.color
#
#     def setborderwidth(self, bw):
#         self.borderwidth = bw
#
#     def getborderwidth(self):
#         return self.borderwidth
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length = 0
#         self.width = 0
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
#
# r=Rectangle()
# r.setlength(20)
# r.setwidth(30)
# r.setcolor("blue")
# r.setborderwidth(100)
#
# print("Length:", r.getlength())
# print("width:", r.getwidth())
# print("color:", r.getcolor())
# print("border width:", r.getborderwidth())

class Shape:
    def __init__(self):
        self.color = " "
        self.border_width = 0

    def setcolor(self, c):
        self.color = c
    def getcolor(self):
        return self.color

    def setborder_width(self, bw):
        self.border_width = bw
    def getborder_width(self):
        return self.border_width

class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def setlength(self, l):
        self.length = l
    def getlength(self):
        return self.length

    def setwidth(self, w):
        self.width = w
    def getwidth(self):
        return self.width

g = Rectangle()
g.setlength(30)
g.setwidth(40)
g.setcolor("Purple")
g.setborder_width(100)

print("Length:", g.getlength())
print("Width:", g.getwidth())
print("Color:", g.getcolor())
print("Border_width:", g.getborder_width())