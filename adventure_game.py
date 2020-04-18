import time   


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2) :
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry,choose another choice.")
    return response


def intro():
    print_pause("Hello! I am Mike, your chef today")
    print_pause("Today we have two dishes for dinner ")
    print_pause("The first is beef ribs with barbecue sauce")
    print_pause("The second is red pasta with tomato sauce")


def get_order():
    response = valid_input("please place your order."
                           "would you like beef ribs or red pasta?\n",
                           "beef ribs", "red pasta")
    if "beef ribs" in response:
        print_pause("Great choice!")
    elif "red past" in response:
        print_pause("Excellent choice")
    print_pause("your order will be ready shortly.")
    order_again()


def order_again():
    response = valid_input("would you like to place another order?"
                          "please say 'yes' or 'no'.\n"
                          "yes","no")
    if "no" in response:
        print_pause("OK, goodbuy!")
    elif "yes" in response:
        print_pause("Sure, I'm happy to take another order.")
        get_order()


def order_dinner():
    intro()
    get_order()
    order_again()

order_dinner()

