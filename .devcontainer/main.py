def modulo_calculator():
    #getting first number, then get the number to mod the first 
    x = input("First number?")
    y = input("Second number?")
    #preforming calculation % = modulo
    z = int(x) % int(y)
    #printing result
    print("The result is " + str(z))

def int_division():
    #Getting the first number to be divieded, the the second number to divied the first by.
    x = int(input("What number would you like divied?"))
    y = int(input("What number would you like to divide by?"))
    #Preforming calculation / = divition 
    z = x / y
    #print calculated result
    print("The result is " + str(z))

def for_loop_counter():

    counter = float(input("What should the starting value of the counter be?"))

    loop_counter = int(input("How many times should the loop run?"))

    increment = float(input("How much should the counter increment by?"))

    is_positive = input("Should the counter decrement instead of incrementing? y / n") == "n"
    
    if not is_positive:
        increment *= -1

    for i in range(loop_counter):
        counter += increment

    print("The final value of the counter is " + str(counter))


def float_int_calculator():
    #getting the float number
    x = float(input("What deimal number would you like to start with would you like?"))
    #getting integer
    y = int(input("What integer would you like to add?"))
    #adding them together
    z = x + y
    #printing result
    print("The result is " + str(z))


def ascii_val():
    user_str = input("Give me a string you would like the ascii values of its chars: \n ")

    for i in range(len(user_str)):
        print("The char at position " + str(i) + " is " + user_str[i] + " and the ASCII value is " + str(ord(user_str[i])))


def change_machine():
    #array for types of coins
    coins = [25, 10, 5]
    #number of each type of coin to needed to give back
    coin_counts = [0, 0, 0]
    #assuming from comments in the 'c' starter code price start at $2
    price = float(2.0)
    #get payment
    payment = float(input("That will be $"+ str(price)+ ". Enter your payment in $"))
    #calculate change in cents
    change = int(100 * (payment - price))
    #process each coin type
    for i in range(len(coins)):
        #Adding as many coins as can fit inside of payment variable
        coin_counts[i] += change // coins[i]
        #Remove these coins from payment
        change %= coins[i]

    #optional rounding
    if change >= 3:
        coin_counts[2] += 1
        change = 0

    print(str(coin_counts[0]) + " quarters, " + str(coin_counts[1]) + " dimes and " + str(coin_counts[2]) + " nickels")
        
def rock_paper_scissor():

    user_c = int(input("make choice"))       


def rps_choice
     
     user_input = int(input("Make a choice. \n 1. Rock \n 2. Paper \n 3.Scissors"))

    if user_input == 1:
        return "rock"

    elif user_input == 2:
        return "paper"

    elif user_input == 3:
        return "Scissors"










user_input = int(input("Which function would you like to run?"))

if user_input == 0:
    modulo_calculator()
elif user_input ==1:
    int_division()
elif user_input == 2:
    for_loop_counter()
elif user_input == 3:
    float_int_calculator()
elif user_input == 4:
    ascii_val()
elif user_input == 5:
    change_machine()
elif user_input == 6:
    rock_paper_sissor()
elif user_input == 7:
    mario_flag() 

