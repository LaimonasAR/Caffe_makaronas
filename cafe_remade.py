from typing import Union
from tables import Reservation


# ------------Not used yet-----------
def input_request(type: str) -> Union[str, int]:
    name = "Enter Your name, please."
    surname = "Enter Your surname, please."
    table_type = "Enter desired table type: Single, Double or Family"
    if type == "name":
        print(name)
    if type == "surname":
        print(surname)

    while True:
        user_input = input("Type here")
        if isinstance(user_input, str):
            return user_input
        else:
            print("Made a mistake maybe?")


# -------------------------------------


def main():
    print("Hello and welcome")
    surname = input("What is Your last name? ")

    if Reservation.check_if_reserved(surname=surname) == True:
        print("Your table is reserved for You")
        # proceed to ordering
    else:
        print("You do not have a reservation")
        table_type = input(
            "What type of table do You want - Single, Double or Family: "
        )
        table = Reservation.reservation(table_type=table_type, surname=surname)
        if isinstance(table, dict):
            for items, values in table.items():
                print(items, "--", values)
        else:
            print(table)


main()
# change

# print(help(Tables))
# main()
