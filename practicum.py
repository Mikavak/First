class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28

    def __init__(self, first_name_value, second_name_value, gender_value):
        self.first_name = first_name_value
        self.second_name = second_name_value
        self.gender = gender_value

# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name_value='Мясинка',
                     second_name_value='Мясковна', gender_value='ж')
employee2 = Employee(first_name_value='Жульбик',
                     second_name_value='Булькович', gender_value='м')

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}',
      f'Фамилия: {employee1.second_name}, Пол: {employee1.gender}',
      f'Отпускных дней в году: {employee1.vacation_days}.')
