#!/usr/bin/python3
"""defines a square class"""


class square():
    """defines a class for square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """check and sets the value"""
        for key, value in kwargs.items():
            if value < 0:
                raise ValueError("Value can't be negative")
            if key in ['width', 'height']:
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Permineter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
