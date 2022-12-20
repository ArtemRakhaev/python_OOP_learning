class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @staticmethod
    def check_size(size):
        return type(size) == int and 0 <= size <= 10000

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.check_size(width):
            if self.__width != width:
                self.__width = width
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check_size(height):
            if self.__height != height:
                self.__height = height
                self.show()
