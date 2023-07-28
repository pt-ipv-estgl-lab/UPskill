'''
Video managment

'''
from product import Product, ProductType

class VideoError(Exception): # Product Errors 
    pass

class Video(Product):
    # Constructor
    def __init__(self, title='No title', 
                 type=ProductType.MOVIE, 
                 buy_date=None,
                 length=None, starring=None):
        super().__init__(title,type, buy_date) # call constructor of super class
        self.set_length(length)
        self.set_starring(starring)

    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        if length != None and length < 0:
            raise VideoError("Error: length can't be < 0")
        self.__length = length

    def get_starring(self):
        return self.__starring

    def set_starring(self, starring):
        if starring != None and len(starring) == 0:
            raise VideoError("Error: starring is not valid")
        self.__starring = starring
            
    def __str__(self):         # textual representation of a product
        return super().__str__() + " | " \
            + str(self.get_length()) + " | " \
            + str(self.get_starring())

if __name__ == '__main__': # for testing propose
    from friend import Friend
    from loan import Loan
    import time
    import random
    from datetime import datetime

    my_media_lib = [Video("Indiana Jones and the Dial of Destiny",
                    buy_date=datetime(2023,7,21),
                    starring=["Harrison Ford", 
                              "Phoebe Waller-Bridge",
                              "Antonio Banderas"])]
     
    try:
        my_media_lib[0].set_length(-1)
    except VideoError as e:
        print(e)
    my_media_lib[0].set_length(154)

    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds

    a_friend = Friend("Kiki", email='kiki@gmail.com')
    a_loan = Loan(my_media_lib[0], a_friend)
    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds
    a_loan.set_end(datetime.now())
    my_media_lib[0].give_back(a_loan)
    a_loan = Loan(my_media_lib[0], Friend("Badass"),end=datetime(2023,8,1))
    time.sleep(random.randint(0,5)) # random value between 0 and 5 seconds

    my_media_lib.append(Product('Python HowTo', type=ProductType.BOOK))
    a_loan = Loan(my_media_lib[1], a_friend, datetime(2023,7,24),datetime(2023,8,14))

    for product in my_media_lib:
        print(product)
        for loan in product.get_loans():
            print('\t', loan, 'to', loan.get_friend())


