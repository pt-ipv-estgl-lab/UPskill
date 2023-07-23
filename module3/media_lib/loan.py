'''
Loan managment

'''
from datetime import datetime
from product import Product
from friend import Friend

class LoanError(Exception): # Product Errors 
    pass

class Loan:
    # Constructor
    def __init__(self, product, friend, init=None, end=None):
        if product is None or friend is None:
            raise LoanError("Error: product or friend is None")
        if not isinstance(product, Product) or not isinstance(friend, Friend):
            raise LoanError("Error: product or friend is invalid")
        self.__product = product
        self.__friend = friend
        self.__init = None
        self.__end = None

        if init is None: # if init is None
            init = datetime.now()  # init is now
        self.set_init(init)    
        self.set_end(end)
        product.create_loan(self) # add the created loan to produt's loans

    def get_product(self):
        return self.__product
    
    def get_friend(self):
        return self.__friend
    
    def set_init(self, init):
        if not isinstance(init, datetime):
            raise LoanError("Error: init date and time is invalid")
        if self.get_end() != None and init >= self.get_end():
            raise LoanError("Error: init >= end")

        self.__init = init

    def get_init(self):
        return self.__init

    def set_end(self, end):
        if end != None and not isinstance(end, datetime):
            raise LoanError("Error: end date and time is invalid")
        
        if end != None and end <= self.get_init():
            raise LoanError("Error: end <= init")

        self.__end = end

    def get_end(self):
        return self.__end

    def __str__(self):      # textual representation of a loan
        return self.get_product().__str__() + " | " \
            + self.get_friend().__str__() + " | " \
            + str(self.get_init()) + " -> " \
            + str(self.get_end())


if __name__ == '__main__': # for testing propose
    import time
    import random

    try:
        a_loan = Loan(None,Friend('Nana'))
    except LoanError as e:
        print(e)

    try:
        a_loan = Loan(Product(),'Nana')
    except LoanError as e:
        print(e)

    a_product = Product()
    print(a_product)
    print()
    a_loan = Loan(a_product, Friend('Teté'))
#    a_product.create_loan(a_loan) # add the loan to products loans
        
    for loan in a_product.get_loans():
        print(loan)
    print()

    try:
        a_loan.set_end(a_loan.get_init()) # test end_date == init_date
    except LoanError as e:
        print(e)
    
    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds
    a_loan.set_end(datetime.now())
    a_product.give_back(a_loan)

    for loan in a_product.get_loans():
        print(loan)
    print()
    from product import ProductType
    other_product = Product("Harry Potter and the Philosopher's Stone",
                            ProductType.BOOK,datetime(2022,10,1))
    other_friend = Friend('Juka','Joaquim Baia','juka@ipg.pt')
    other_loan = Loan(other_product, other_friend,
                      datetime.now(),datetime(2023,7,31))
    for loan in other_product.get_loans():
        print(loan)
    print()
    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds
    other_loan.set_end(datetime.now())
    other_product.give_back(other_loan)

    for loan in other_product.get_loans():
        print(loan)
    print()
    
