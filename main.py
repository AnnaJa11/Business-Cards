from faker import Faker
fake = Faker()

class Card:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # variable
        self.max_signs = 15
        self._name_length = 0

    # def __str__(self):
    #     return f'Card(first_name={self.first_name}, last_name = {self.last_name}, email= {self.email}'
    def __repr__(self):
        return f'Card(first_name={self.first_name}, last_name = {self.last_name}, email= {self.email}'
    def contact(self):
        return f'Kontaktuję się z {self.first_name} {self.last_name} {self.email}'
    
    @property
    def label_length(self):
        name_signs = len(self.first_name+' '+self.last_name)
        return name_signs
    
    @label_length.setter                            # nie dziala setter, nie sprawdza wartosci pod if  !!!!!
    def label_length(self, value):
        if value <= self.max_signs:
            self._name_length = value
            print(f'OK. The name lengh does not exceed the limit of signes in 1 line.')
        else:
            raise ValueError(f"Number of signes {value} exceeds max signes in line {self.max_signs}")
        

class BaseContact(Card):
    def __init__(self, mobile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mobile = mobile
    
    def __repr__(self):
        return f'first_name={self.first_name}, last_name = {self.last_name}, email= {self.email}, mobile={self.mobile}'
 
    def contact(self):
        return f'Wybieram numer {self.mobile} i dzwonię do {self.first_name} {self.last_name}.'

class BusinessContact(Card):
    def __init__(self, company, occupation, office_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.occupation = occupation
        self.office_phone = office_phone

    def __repr__(self):
        return f'first_name={self.first_name}, last_name = {self.last_name}, email= {self.email}, company= {self.company}, occupation={self.occupation}, office_phone={self.office_phone}'

    def contact(self):
        return f'Wybieram numer {self.office_phone} i dzwonię do {self.first_name} {self.last_name}.'
    
base_cards = []
business_cards = []
want_create = True
while want_create:
   card_type = int(input("Enter: 1 for 'base_cards' or 2 for 'business_cards'"))
   card_quantity = int(input('Enter how many cards should be created: '))
   def create_contacts(card_type, card_quantity):
       if card_type == 1:
         for i in range (0,card_quantity):
            base_card = [BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.ascii_free_email(), mobile= fake.phone_number())]
            base_cards.append(base_card)
       elif card_type == 2:
         for i in range (0,card_quantity):
            business_card = [BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(), email=fake.ascii_free_email(), office_phone= fake.msisdn())]
            business_cards.append(business_card)
         
   create_contacts(card_type, card_quantity) 

   if card_type == 1:
          [print(f'{card}\n') for card in base_cards]    
   elif card_type == 2:
          [print(f'{card}\n') for card in business_cards]
   
   create_more = input('Would you like to create more cards? y/n: ')
   if create_more == 'n':
       want_create = False
       print('The program is closing now ...')
          
# print(f'My cards:\n')
# for num in range (0, len(base_cards)):
#     print(f'{base_cards[num]}\n')

# sorted_by_fname = sorted(base_cards, key=lambda card: card.first_name)
# print(f'Sorted by first name:{sorted_by_fname}\n')

# sorted_by_lname = sorted(base_cards, key=lambda card: card.last_name)
# print(f'Sorted by last name: {sorted_by_lname}.')

# sorted_by_email = sorted(base_cards, key=lambda card: card.email)
# print(f'Sorted by emial:{sorted_by_email}.')
        
# print(business_card1.first_name, business_card1.last_name)
# print(business_card1.label_length)
# print(business_card1.contact())
