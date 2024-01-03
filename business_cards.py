class BaseContact:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
        # variable
        self._name_length = 0
        self.max_signs = 10
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.mobile}'

    def contact(self):
        return f'Wybieram numer {self.mobile} i dzwonie do {self.first_name} {self.last_name}.'

    @property
    def label_length(self):
        return self._name_length
    
    @label_length.setter
    def label_length(self, a):
        a = int(self.first_name+' '+self.last_name)
        if a <= self.max_signs:
            self._name_length = a
        else:
            raise ValueError(f"Number of signes {a} exceeds max signes in line {self.max_signs}")


class BusinessContact(BaseContact):
    def __init__(self, occupation, company, office_phone ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company = company
        self.office_phone = office_phone
        label_length = 0

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.office_phone}'

    def contact(self):
        return f'Wybieram numer {self.office_phone} i dzwonie do {self.first_name} {self.last_name}.'
    

card1 = BaseContact(first_name='Laura', last_name='Welch', company="Cosmopolitan", occupation="accountant", email='laura.welch@test.com')

card2 = BaseContact(first_name='Leo', last_name='Michaels', company="Impact Ltd", occupation="designer", email='leo.michaels@test.com')

card3 = BaseContact(first_name='Naomi', last_name='Norack', company="BMI Ltd", occupation="lawyer", email='naomi.norack@test.com')

card4 = BaseContact(first_name='Jack', last_name='Damon', company="Italian Style", occupation="Sales Manager", email='jack.damon@test.com')

card5 = BaseContact(first_name='Peter', last_name='Brown', company="ABD Consulting", occupation="Marketing Manager", email='aapeter.brown@test.com')

cards_list = [card1,card2, card3, card4, card5]


print(card2.name_length)

print(f'My cards:\n')
for num in range (0, len(cards_list)):
    print(f'{cards_list[num]}\n')
