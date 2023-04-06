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

    #in_positive = bool(input("Should the counter decrement instead of incrementing? y / n"))
    

    #for i in increment:
        #print("This loop is running for the "+ str(i+1) +" time.")


def float_int_calculator():

    x = float(input("What deimal number would you like to start with would you like?"))

    y = int(input("What integer would you like to add?"))

    z = x + y

    print("The result is " + str(z))


def ascii_val():
    
    user_str = input("Give me a string you would like the ascii values of its chars: \n ")

    str_size = len(user_str)

    i = 0

    sum = 0

    while(i < str_size):

        sum = sum + ord(user_str[i])
        i = i + 1

    print("The sum  of all these ASCII values is ", sum)


def change_machine():

    coins = array(int[25, 10, 5])







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
    string_flipper()

