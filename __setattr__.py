import time


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if hasattr(self, 'date'):
            return None
        super().__setattr__(key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if hasattr(self, 'date'):
            return None
        super().__setattr__(key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if hasattr(self, 'date'):
            return None
        super().__setattr__(key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = []
        self.slots = ['empty', 'empty', 'empty']

    def add_filter(self, slot_num, filter):
        if (slot_num == 1 and self.slots[0] == 'empty') and isinstance(filter, Mechanical):
            self.slots[0] = 'busy'
            self.filters.insert(0, filter)
        if (slot_num == 2 and self.slots[1] == 'empty') and isinstance(filter, Aragon):
            self.slots[1] = 'busy'
            self.filters.insert(1, filter)
        if (slot_num == 3 and self.slots[2] == 'empty') and isinstance(filter, Calcium):
            self.slots[2] = 'busy'
            self.filters.insert(2, filter)

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = 'empty'
        self.filters.pop(slot_num - 1)

    def get_filters(self):
        return tuple(self.filters)

    def check_filter(self, slot):
        return 0 <= (time.time() - self.filters[slot - 1].date) <= self.MAX_DATE_FILTER

    def water_on(self):
        if 'empty' not in self.slots and len(self.filters) == 3:
            return all(self.check_filter(i) for i in range(1, 4))
        return False


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
my_water.add_filter(3, Calcium(time.time()))
f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)
my_water.add_filter(1, Mechanical(time.time()))
f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)
my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
my_water.water_on()
