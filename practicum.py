class Phone:

    line_type = 'Проводной'

    def __init__(self, dial_line_type) -> None:
        self.dial_line = dial_line_type

    def ring(self):
        print('zzzzzz')

    def call(self, phone_number):
        print(
            f'я звоню по номеру {phone_number}',
            f'использую тип для связи: {self.line_type}.')
        
new_phone = Phone('дисковый')
new_phone.call('555-55-55')
