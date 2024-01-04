# # class BaseContact:
# #     def __init__(self, name, surname, email, phone):
# #        self.name = name
# #        self.surname = surname
# #        self.email = email
# #        self.phone = phone
# #        self._name_sum = 0


# # class BusinessContact(BaseContact):
# #     def __init__(self, occupation, company, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.occupation = occupation
# #         self.company = company
        
# #     def contact(self):
# #         return f'Wybieram numer {self.phone} i dzwonie do {self.name} {self.surname}.'

    
# #     def __repr__(self):
# #         return f'{self.name} {self.surname} {self.phone}'
    
    
    
# #     @property
# #     def name_sum(self):
# #         return self._name_sum
    
# #     @name_sum.setter
# #     def name_sum(self, a):
# #         a = (len(self.name)+ ' '+ len(self.surname))
# #         self._name_sum = a

# #     lisa_b = BaseContact(name='Lisa',surname='Be',email='lisa.be@test.com',phone='123 456 789')

# #     print(lisa_b.contact())

class Car:
  def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self._current_speed = 0
  
  def accelerate(self, step=10):
        self.current_speed += step

  def decelerate(self, step=10):
        self.current_speed -= step

  def __repr__(self):
      return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"

  @property
  def current_speed(self):
        return self._current_speed

  @current_speed.setter
  def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

# # car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
# # print(car._current_speed)

# # car.accelerate()
# # print(car.current_speed)

# # car.accelerate(50)
# # print(car.current_speed)

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
# car.current_speed = 100
# print(car._current_speed)

# # car.current_speed = 400   # wyrzuci blad o przekroczeniu predkosci

# class Truck(Car):
#    def __init__(self, max_load, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.max_load = max_load

# truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
# print(truck)
# truck.current_speed = 
# print(truck.current_speed)

# # truck.accelerate()
# # print(truck.current_speed)

# # print(isinstance(car, Truck))
# # print(isinstance(car, Car))
# # print(isinstance(truck, Car))
# # print(isinstance(truck, Truck))

# # print(issubclass(Truck, Car))
# # print(issubclass(Car, Truck))

# ----------------------------------------
# from faker import Faker
# fake = Faker()
# from main import BaseContact

# base_cards = []
# def create_contacts():
#    for i in range (0,5):
#       BaseContact(first_name=fake.first_name(), 
#                               last_name=fake.last_name(), 
#                               email=fake.ascii_free_email(), 
#                               mobile= fake.phone_number())
#       base_cards.append(base_card)
# print(base_cards)



# base_card1 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.ascii_free_email(), mobile= fake.phone_number())

# base_card2 = BaseContact(first_name='Leo', last_name='Michaels', email='leo.michaels@test.com', mobile= '56688444')

# base_card3 = BaseContact(first_name='Naomi', last_name='Norack', email='naomi.norack@test.com', mobile= '84456142')

# base_card4 = BaseContact(first_name='Jack', last_name='Damon', email='jack.damon@test.com', mobile= '77888844')

# base_card5 = BaseContact(first_name='Peter', last_name='Brown', email='aapeter.brown@test.com', mobile= '111118844')


# business_card1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(), email=fake.ascii_free_email(), office_phone= fake.msisdn())

# business_card2 = BusinessContact(first_name='Leo', last_name='Michaels', company="Impact Ltd", occupation="designer", email='leo.michaels@test.com', office_phone= '00688444')

# business_card3 = BusinessContact(first_name='Naomi', last_name='Norack', company="BMI Ltd", occupation="lawyer", email='naomi.norack@test.com', office_phone= '00456142')

# business_card4 = BusinessContact(first_name='Jack', last_name='Damon', company="Italian Style", occupation="Sales Manager", email='jack.damon@test.com', office_phone= '00888844')

# business_card5 = BusinessContact(first_name='Peter', last_name='Brown', company="ABD Consulting", occupation="Marketing Manager", email='aapeter.brown@test.com', office_phone= '001118844')
# -----------------------
# def decorator(f):
#     def new_function():
#         print("Extra Functionality")
#         f()
#     return new_function

# @decorator
# def initial_function():
#     print("Initial Functionality")

# initial_function()
# -------------------------------------


class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	# @price.deleter
	# def price(self):
	# 	del self._price

house = House(50000.0)  # Create instance
house.price = 45000.0   # Update value
print(house.price) 