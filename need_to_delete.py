class Employee:
    vacation_days = 28
    

    def __generate_employee_id(self, first_name, second_name, gender):
        gen_name = hash(first_name + second_name + gender)
        #return gen_name
    
    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        self._employee_id = self.__generate_employee_id(first_name, second_name, gender)


    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee.
class FullTimeEmployee(Employee):

    def get_unpaid_vacation(self, date_n, no_pay):
        return f'Начало неоплачиваемого отпуска: {date_n}, продолжительность: {no_pay} дней.'


class PartTimeEmployee(Employee):

    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        self.remaining_vacation_days = PartTimeEmployee.vacation_days
        super().__init__(first_name, second_name, gender)

    def __str__(self):
        return f'{self.first_name}, {self.second_name}'


man_1 = FullTimeEmployee(first_name='Mik', second_name='Ava', gender='m')
man_2 = PartTimeEmployee(first_name='Nata', second_name='Ava', gender='w')

print(man_1.get_unpaid_vacation('2023-07-01', 5))

# Пример использования:
# full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee)
print(man_1._employee_id)