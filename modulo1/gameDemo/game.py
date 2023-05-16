import random
'''
Um script que permita ao utilizador adivinhar um número considerado à partida. 
O processo deverá repetir-se até o utilizador introduzir o palpite correto.
Algoritmo 2
'''
secret_number = random.randint(1, 1000) # número a adivinhar

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Enter the number: "))

while user_number != secret_number:
    if user_number > secret_number:
        print("Ha ha! The secret number is lower")
    else:
        print("Ha ha! The secret number is higher")

    user_number = int(input("Enter the number again (0 to quit): "))
    if not user_number:
        break
if secret_number == user_number:
    print(secret_number, "Well done, muggle! You are free now.")
else:
    print('Next time! the secrete number was', secret_number)
