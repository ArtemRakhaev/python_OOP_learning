class Shop:
    def __init__(self, name):
        self.goods = []
        self.name = name

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    new_id = 1
    instances = {'name': (str,), 'weight': (int, float), 'price': (int, float)}

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product.new_id
        Product.new_id += 1

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(self, item)

    def __setattr__(self, key, value):
        if key in self.instances and type(value) not in self.instances[key]:
            if (key == 'weight' or key == 'price') and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.instances:
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(self, key, value)
