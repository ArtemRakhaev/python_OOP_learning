class Track:

    def __init__(self, x, y):
        self.coords = []
        self.x = x
        self.y = y

    def check_coord(self, indx):
        if type(indx) != int or 0 > indx > len(self.coords) - 1:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        self.check_coord(key)
        self.coords[key][1] = value

    def __getitem__(self, item):
        self.check_coord(item)
        return self.coords[item]

    def add_point(self, x, y, speed):
        tpl = [(x, y), speed]
        self.coords.append(tpl)


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError