class Card:
    def __init__(self, first_name, last_name, company, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.occupation = occupation
        self.email = email

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

removed_set  = ['company', 'occupation']


for record in my_cards:
    for key, value in record.items():
        if key not in removed_set:
            print(value)



