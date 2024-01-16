class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type):
        self.dial_type = dial_type

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    def __str__(self):
        return f'У мобильного телефона {self.dial_type}  номера'


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type, network_type):
        self.network_type = network_type
        super().__init__(dial_type)

    def ring(self):
        print('Дзынь-дзынь!')

    def start_game(self):
        print('Игра запущена!')

    def __str__(self):
        return f'У мобильного телефона {self.dial_type} тип набора номера'
    
    def __get_vacation_salary(self):
        return (0.8 * self.__salary)

    # Здесь переопределён метод __str__ .


mob_1 = Phone('дисковый')
mob_2 = MobilePhone('мобильный','LTE')

mob_1.ring()
mob_2.ring()
#full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

# part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
# part_time_employee.consume_vacation(5)
# print(part_time_employee.get_vacation_details())