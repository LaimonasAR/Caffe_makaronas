import datetime


class TableReservation:
    current_time = datetime.datetime.now()
    data_base_of_tabe = {
        "single": {"1": "free", "2": "free", "3": "free", "4": "free"},
        "double": {"5": "free", "6": "free", "7": "free"},
        "family": {"8": "free", "9": "free"},
    }

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def check_reservation(self) -> None:
        print(f"Welcome {self.name}, {self.surname} to our restaurant")
        time = lambda t: t.strftime("%H:%M:%S")
        print(f"Current time is: {time(self.current_time)}")
        check = False
        if self.name and self.surname == "Admin":
            self.print_info_of_reservation()
        else:
            for split_by_teble_types in self.data_base_of_tabe.values():
                for (
                    table_number,
                    table_reservation_check,
                ) in split_by_teble_types.items():
                    if table_reservation_check != "free":
                        if self.name and self.surname in table_reservation_check:
                            # print(table_reservation_check)
                            get_info = table_reservation_check.split(", ")
                            check = True
                            reservation = f"Your {get_info[0]} {get_info[1]} table is: {table_number}"
                            print(reservation)

            if check == False:
                print("You do not have a reservation")
                self.get_reservation()
        self.print_info_of_reservation()

    def print_info_of_reservation(self):
        for table_type, table_reservation in self.data_base_of_tabe.items():
            print("\nTable ID:", table_type)
            for key in table_reservation:
                print(key + ":" + table_reservation[key])

    def get_reservation(self):
        number_of_guests = int(input("Please enter the number of guests: "))
        if number_of_guests == 1:
            number_of_guests = self.data_base_of_tabe["single"]
        elif number_of_guests == 2:
            number_of_guests = self.data_base_of_tabe["double"]
        elif number_of_guests > 2:
            number_of_guests = self.data_base_of_tabe["family"]
        for table, reservation in number_of_guests.items():
            # print(f'{single_table} ":" {reservation}')
            if reservation != "free":
                print("Sorry reservation is not posible")
                break
            else:
                table_reservation_time = str(
                    input("Please enter time for reservation: ")
                )
                number_of_guests[
                    table
                ] = f"{self.name} {self.surname} {table_reservation_time}"
                print(
                    f"{self.name}, {self.surname} your table is: {table} reserved at {table_reservation_time} o'clock"
                )
                break
        print(self.data_base_of_tabe)


name = input("Please enter your name: ").capitalize()
surname = input("Please enter your surname: ").capitalize()
person = TableReservation(name=name, surname=surname)
TableReservation.data_base_of_tabe["single"]["1"] = "Tim, Smith, 16:00"
TableReservation.data_base_of_tabe["double"]["6"] = "Tomas, Popovas, 16:00"
TableReservation.data_base_of_tabe["family"]["8"] = "Mindaugas, Nauseda, 14:00"
TableReservation.data_base_of_tabe["family"]["9"] = "Jonas, Hansen, 14:00"
person.check_reservation()
