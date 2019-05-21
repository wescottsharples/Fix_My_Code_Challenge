#!/usr/bin/python3
"""
Contains Square class
"""


class Square():
    """
    Defines Square class
    """
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.width and self.width != self.height:
            self.height = self.width
        elif self.width != self.height:
            self.width = self.height

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perim(self):
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perim())
