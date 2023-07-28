'''
Products managment

'''

from enum import Enum
from datetime import datetime

class ProductError(Exception): # Product Errors 
    pass

class ProductType(Enum):
    BOOK = 0
    MAGAZINE = 1
    MOVIE = 2
    GAME = 3
    ALBUM = 4
    OTHER = 5

class Product:
    __id = 1
    # Constructor
    def __init__(self, title='No title', 
                 type=ProductType.OTHER, 
                 buy_date=None):
        self.__id = Product.__id
        self.set_title(title)
        self.set_type(type)
        if buy_date == None: # if buy_date is None
            buy_date = datetime.today()  # buy_date is today
        self.set_buy_date(buy_date)    
        self.__borrowed = False
        self.__loans = []
        Product.__id+=1

    def get_id(self):
        return self.__id
    
    def set_title(self, title):
        if title != None and not len(title):
            raise ProductError("Error: title can't be empty")
        self.__title = title

    def get_title(self):
        return self.__title

    def set_type(self, type):
        if not isinstance(type, ProductType):
            raise ProductError("Error: type " + 
                               str(type) + " is not valid")
        self.__type = type
    
    def get_type(self):
        return self.__type

    def is_borrowed(self):
        return self.__borrowed

    def set_buy_date(self, date):
        if date != None and not isinstance(date, datetime):
            raise ProductError("Error: date is invalid")
        self.__purchase_date = date

    def get_buy_date(self):
        return self.__purchase_date

    def create_loan(self, loan):
        if self.is_borrowed():
            raise ProductError("Error: "+ 
                               self.get_title() +
                               " is borrowed!")
        self.__loans.append(loan)
        self.__borrowed = True

    def give_back(self, loan):
        if not self.is_borrowed():
            raise ProductError("Error: "+ 
                               self.get_title() +
                               " is not borrowed!")

        if loan not in self.__loans:
            raise ProductError("Error: "+ 
                               self.get_title() +
                               " is not borrowed to " + 
                               str(loan))
        self.__borrowed = False

    def get_loans(self):
        return self.__loans[:]
            
    def __str__(self):         # textual representation of a product
        return str(self.get_id()) + " | " \
            + self.get_title() + " | " \
            + str(self.get_type()) + " | " \
            + str(self.get_buy_date()) + " | " \
            + str(self.is_borrowed())


if __name__ == '__main__': # for testing propose
    try:
        a_product = Product(type=5)
    except ProductError as e:
        print(e)
    a_product = Product()
    print(a_product)
    other_product = Product('Python how to', 
                            type=ProductType.BOOK,
                            buy_date=datetime(2023,5,31))
    print(other_product)

    try:
        other_product = Product('')
    except ProductError as e:
        print(e)

    try:
        other_product = Product(type='GAME')
    except ProductError as e:
        print(e)

    another_product = Product()
    print(another_product)
    another_product.set_buy_date(None)
    print(another_product)

    other_product.create_loan('my loan')
    print(other_product, ':', sep='', end='')
    print(other_product.get_loans())

    try:
        other_product.give_back('other loan')
    except ProductError as e:
        print(e)

    try:
        other_product.create_loan('other loan')
    except ProductError as e:
        print(e)

    other_product.give_back('my loan')
    print(other_product, ':', sep='', end='')
    print(other_product.get_loans())
    other_product.create_loan('other loan')
    print(other_product, ': ', sep='', end='')
    print(other_product.get_loans())
