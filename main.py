class Card:
    def __init__(self, first_name, last_name, company, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.occupation = occupation
        self.email = email
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

my_cards = [
    {'first_name':'Laura', 
     'last_name': 'Welch', 
     'company': "Cosmopolitan", 
     'occupation': "accountant", 
     'email': 'laura.welch@test.com'},

      {'first_name':'Leo', 
     'last_name': 'Michaels', 
     'company': "Impact Ltd", 
     'occupation': "designer", 
     'email': 'leo.michaels@test.com'},

      {'first_name':'Naomi', 
     'last_name': 'Norack', 
     'company': "BMI Ltd", 
     'occupation': "lawyer", 
     'email': 'naomi.norack@test.com'},

      {'first_name':'Jack', 
     'last_name': 'Damon', 
     'company': "Italian Style", 
     'occupation': "Sales Manager", 
     'email': 'jack.damon@test.com'},

      {'first_name':'Peter', 
     'last_name': 'Brown', 
     'company': "ABD Consulting", 
     'occupation': "Marketing Manager", 
     'email': 'peter.brown@test.com'},

]

my_cards_length = len(my_cards)

card1 = Card(first_name='Laura', last_name='Welch', company="Cosmopolitan", occupation="accountant", email='laura.welch@test.com')

card2 = Card(first_name='Leo', last_name='Michaels', company="Impact Ltd", occupation="designer", email='leo.michaels@test.com')

card3 = Card(first_name='Naomi', last_name='Norack', company="BMI Ltd", occupation="lawyer", email='naomi.norack@test.com')

card4 = Card(first_name='Jack', last_name='Damon', company="Italian Style", occupation="Sales Manager", email='jack.damon@test.com')

card5 = Card(first_name='Peter', last_name='Brown', company="ABD Consulting", occupation="Marketing Manager", email='peter.brown@test.com')

cards_list = []

for i in range(len(my_cards)):
    cards_list.append(f'card{i+1}')
print(cards_list)


