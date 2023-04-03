class Tables:
    def __init__(self) -> None:
        self.all_tables = {
            1: {
                "Table Number": 1,
                "Table type": "Single",
                "Reserved": True,
                "Surname": "Jordan",
            },
            2: {
                "Table Number": 2,
                "Table type": "Single",
                "Reserved": True,
                "Surname": "Johnson",
            },
            3: {
                "Table Number": 3,
                "Table type": "Single",
                "Reserved": True,
                "Surname": "Pierce",
            },
            4: {
                "Table Number": 4,
                "Table type": "Double",
                "Reserved": False,
                "Surname": "",
            },
            5: {
                "Table Number": 5,
                "Table type": "Double",
                "Reserved": False,
                "Surname": "",
            },
            6: {
                "Table Number": 6,
                "Table type": "Double",
                "Reserved": True,
                "Surname": "Jackson",
            },
            7: {
                "Table Number": 7,
                "Table type": "Family",
                "Reserved": True,
                "Surname": "Sparrow",
            },
            8: {
                "Table Number": 8,
                "Table type": "Family",
                "Reserved": True,
                "Surname": "Adams",
            },
            9: {
                "Table Number": 9,
                "Table type": "Family",
                "Reserved": False,
                "Surname": "",
            },
            10: {
                "Table Number": 10,
                "Table type": "Family",
                "Reserved": False,
                "Surname": "",
            },
        }

    def check_reservetion(self, surname: str) -> bool:
        reserved_table = False
        for table_number, table_data in self.all_tables.items():
            for key, value in table_data.items():
                if (
                    table_data["Reserved"] == True
                    and (table_data["Surname"]).upper() == surname.upper()
                ):
                    reserved_table = True
                    return reserved_table
        return reserved_table

    def reserve_table(self, type: str, surname: str) -> dict:
        free_table = False
        for table_number, table_data in self.all_tables.items():
            for key, value in table_data.items():
                if table_data["Reserved"] == False and table_data["Table type"] == type:
                    table_data["Surname"] = surname
                    table_data["Reserved"] = True
                    free_table = True
                    return table_data

        if free_table == False:
            return f"Sorry {surname}, there is no free {type} table right now"

    def short_check(self):
        for table_number, table_data in self.all_tables.items():
            # print(f"{table_number}")

            for key, value in table_data.items():
                print(key, value)


def check_if_reserved(surname) -> bool:
    my_table = Tables()
    reserved = my_table.check_reservetion(surname=surname)
    return reserved


def reservation(table_type, surname) -> None:
    my_table = Tables()
    table = my_table.reserve_table(type=table_type, surname=surname)
    if isinstance(table, dict):
        for items, values in table.items():
            print(items, "--", values)
    else:
        print(table)


def main():
    print("Hello and welcome")
    surname = input("What is Your last name? ")
    if check_if_reserved(surname=surname) == True:
        print("Your table is reserved for You")
        # proceed to ordering
    else:
        print("You do not have a reservation")
        table_type = input(
            "What type of table do You want - Single, Double or Family: "
        )
        reservation(table_type=table_type, surname=surname)


main()


# print(help(Tables))
# main()
