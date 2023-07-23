'''
loan managment

'''

import re # using regular expression 

class FriendError(Exception): # Friend management errors 
    pass

class Friend:
    def __init__(self, nickname, name = None, email = None): # Constructor
        self.__nickname = nickname
        self.set_name(name)
        self.set_email(email)

    def get_nickname(self):
        return self.__nickname
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        # name == None is valid (does not exist)
        if name != None and len(name) == 0:
            raise FriendError("Error: name can't be empty")
        self.__name = name
        
    def get_email(self):
        return self.__email

    def set_email(self, email):
        # email == None is valid (does not exist)
        if email != None: self.__check(email)
        self.__email = email

    def __str__(self):       # textual representation of a friend (is nickname)
        return self.get_nickname()

    def __check(self, email):
        # Make a regular expression
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # pass the regular expression
        # and the string into the fullmatch() method
        if( email != None and not re.fullmatch(regex, email)):
            raise FriendError('Error: Invalid email address '+ email)

if __name__ == '__main__': # for testing propose

    my_friend = Friend('red')
    print(my_friend)
    try:                        # test if name can be empty ""
        my_friend.set_name("")
    except FriendError as e:
        print(e)

    my_friend.set_name("Justina Maria") # test setter of the name
    print(my_friend.get_name())

    try:
        my_friend.set_email("justina@gmail") # test if emaif is verified
        print(my_friend.get_email())
    except FriendError as e:
        print(e)
    
    try:
        my_friend.set_email("justina") # test 2 if emaif is verified
        print(my_friend.get_email())
    except FriendError as e:
        print(e)

    try:
        my_friend.set_email("justina@estgl.ipv.pt") # test 3 if emaif is verified
        print(my_friend.get_email())
    except FriendError as e:
        print(e)

    print(my_friend.get_email()) # get the correct email

    try:                        # test Constructor with all parameters 
        other_friend = Friend('blond','Antonina','antonina@gmail')
    except FriendError as e:
        print(e)

    other_friend = Friend('blond','Antonina','antonina@outlook.com')
    print(other_friend.get_nickname())
    print(other_friend.get_name())
    print(other_friend.get_email())
    other_friend.__check('ccosta@estgl.ipv.pt') # test if utility method can be used