import modulo

my_list = [2,4,6,10]

print('sum=', modulo.suml(my_list))
print('prod=', modulo.prodl(my_list))
print('number of calls=', modulo.__counter)

import sys

for p in sys.path:
    print(p)



