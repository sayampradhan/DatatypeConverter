#importing neccessary modules
from fileinput import close
from pdb import Restart

# define functions for type conversion
#function for integer to string
def int_to_str():
    user_input = int(
        input("Write an integer to convert: ")
        )

    result = str(user_input)

    print("Hurreyyy! Your integer is converted into string")
    print("The string is", result)
    print('New datatype is', type(result))


#function for float to string
def float_to_str():
    user_input = float(
        input("Write a float to convert: ")
        )

    result = str(user_input)

    print("Hurreyyy! Your float is converted into string")
    print("The new string is", result)
    print('New datatype is', type(result))


#function for integer to float
def int_to_float():
    user_input = int(
        input("Write an integer to convert: ")
        )

    result = float(user_input)

    print("Hurreyyy! Your integer is converter into float")
    print("The new float is", result)
    print('New datatype is', type(result))


#function for float to integer
def float_to_int():
    user_input = float(
        input("Write a float to convert: ")
        )

    result = int(user_input)

    print("Hurreyyy! Your float is converted into integer")
    print("The new integer is", result)
    print('New datatype is', type(result))


#function for list to tuple
def list_to_tuple():
    list = []
    new_tuple = ()
    no_of_elements = int(input(
        "Write the number of elements you want to add to your list: "
    ))

    for i in range(no_of_elements):
        input_elements = input(
        'Write the element: '
        )

        list.append(input_elements)

    for i in list:
        new_tuple = new_tuple+(i,)

    print("Original List is:", list)

    result = new_tuple

    print("Hurreyyy! Your list is converted into tuple")
    print('New tuple is', new_tuple)
    print('New datatype is', type(result))


#function for tuple to list
def tuple_to_list():
    new_list = []
    tuple = ()
    no_of_elements = int(input(
        "Write the number of elements you want to add to your tuple: "
    ))

    for i in range(no_of_elements):
        input_elements = input(
        'Write the element: '
        )

        tuple = tuple + (input_elements,)

    for i in tuple:
        new_list.append(i)

    print("Original List is:", list)

    result = new_list

    print("Hurreyyy! Your tuple is converted into list")
    print('New tuple is', new_list)
    print('New datatype is', type(result))



# MAIN
#message display
print(
    "WELCOME TO A SIMPLE TYPE CONVERSION\n"
    "\n"
    "Choose a number\n"
    "1 =======> Integer to String\n"
    "2 =======> Integer to Float\n"
    "3 =======> Float to String\n"
    "4 =======> Float to Integer\n"
    "5 =======> List to Tuple\n"
    "6 =======> Tuple to List\n"
)

#user input
user_choice = int(input(
    "Write your choice here: "
    ))

#conditions
while True:
    if user_choice==1:
        int_to_str()
        break

    elif user_choice==2:
        int_to_float()
        break

    elif user_choice==3:
        float_to_str()
        break

    elif user_choice==4:
        float_to_int()
        break

    elif user_choice==5:
        list_to_tuple()
        break

    elif user_choice==6:
        tuple_to_list()
        break

    else:
        print("Invalid Choice!")
        break


print("Thanks for using our app!!!")