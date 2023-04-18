from typing import List, Union
all_tables = [
    {
        "Table Number": 1,
        "Table type": "Single",
        "Reserved": True,
        "Surname": "Jordan",
    },
    {
        "Table Number": 2,
        "Table type": "Single",
        "Reserved": True,
        "Surname": "Johnson",
    },
    {
        "Table Number": 3,
        "Table type": "Single",
        "Reserved": True,
        "Surname": "Pierce",
    },
    {
        "Table Number": 4,
        "Table type": "Double",
        "Reserved": False,
        "Surname": "",
    },
    {
        "Table Number": 5,
        "Table type": "Double",
        "Reserved": False,
        "Surname": "",
    },
    {
        "Table Number": 6,
        "Table type": "Double",
        "Reserved": True,
        "Surname": "Jackson",
    },
    {
        "Table Number": 7,
        "Table type": "Family",
        "Reserved": True,
        "Surname": "Sparrow",
    },
    {
        "Table Number": 8,
        "Table type": "Family",
        "Reserved": True,
        "Surname": "Adams",
    },
    {
        "Table Number": 9,
        "Table type": "Family",
        "Reserved": False,
        "Surname": "",
    },
    {
        "Table Number": 10,
        "Table type": "Family",
        "Reserved": False,
        "Surname": "",
    },
]


class Tables:
    def __init__(self, all_tables_list: List[dict]) -> None:
        self.all_tables_list = all_tables_list

    def check_reservation(self, surname: str) -> bool:
        reserved_table = False
        for table_data in self.all_tables_list:
            for key, value in table_data.items():
                if (
                    table_data["Reserved"] == True
                    and (table_data["Surname"]).upper() == surname.upper()
                ):
                    reserved_table = True
                    return reserved_table
        return reserved_table

    def reserve_table(self, type: str, surname: str) -> Union[dict, str]:
        free_table = False
        for table_data in self.all_tables_list:
            for key, value in table_data.items():
                if table_data["Reserved"] == False and table_data["Table type"] == type:
                    table_data["Surname"] = surname
                    table_data["Reserved"] = True
                    free_table = True
                    return table_data

        if free_table == False:
            return f"Sorry {surname}, there is no free {type} table right now"

    def short_check(self):
        for table_number, table_data in self.all_tables_list:
            # print(f"{table_number}")

            for key, value in table_data.items():
                print(key, value)

class Reservation:

    def check_if_reserved(surname) -> bool:
        my_table = Tables(all_tables)
        reserved = my_table.check_reservation(surname=surname)
        return reserved
    
    def reservation(table_type, surname) -> None:
        my_table = Tables(all_tables)
        table = my_table.reserve_table(type=table_type, surname=surname)
        return table