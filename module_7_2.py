def __str__(self):
    return f"{self.name}, {self.weight}, {self.category}"

def get_products(self):
    try:
        with open(self.__file_name, 'r') as file:
            return
        '/n' .join([line.strip() for line in file])
    except FileExistsError:
        return ''

def add(self, *products):
    products_in_file = self.get_products().split('/n')
    for product in products:
        if f"{product.name}, {product.weight}, {product.category}" not in products_in_file:
            with open(self.__file_name, 'a') as file:
                file.write(f'{product.name}, {product.weight}, {product.category} /n')
        else:
            print(f'Продукь {product.name} уже есть в магазине')