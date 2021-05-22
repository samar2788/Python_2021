bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
for bicycle in bicycles:
	print(bicycle)

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = f"My first bicycle was {bicycles[2].title()}"
print(message)

friends=['Shashank','Anupama','Siddharth','Divya']

for friend in friends:
	print(f"Hi {friend} whats up?")

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

guests = ['Shashank','Hank Moody','Tony']

for guest in guests:
	print(f"{guest} you are cordially invited to a formal dinner please come if you can")

print(f"It seems that {guests[2]} could not make it to dinner")

guests[2]='Nina Hartley'

for guest in guests:
	print(f"{guest} you are cordially invited to a formal dinner please come if you can")

print("It seems a bigger table is available and more guests can be invited")

guests.insert(0,'Stormy Daniels')
guests.insert(1,'Megan Rain')
guests.append('Mia Khalifa')

for guest in guests:
	print(f"{guest} you are cordially invited to a formal dinner please come if you can")

print('Apologies everyone i can only invite two people to dinner so rest of you can fuck off')

pop_guest=guests.pop()
print(f"{pop_guest} you can kindly fuck off")
pop_guest=guests.pop()
print(f"{pop_guest} you can kindly fuck off")
pop_guest=guests.pop()
print(f"{pop_guest} you can kindly fuck off")
pop_guest=guests.pop()
print(f"{pop_guest} you can kindly fuck off")

for guest in guests:
	print(f"{guest} you are cordially invited to a formal dinner please come if you can")

del guests[-1]
del guests[0]

print(guests)

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']

print("Here is the original list of cars")
print(cars)

print("Here is a sorted list of cars")
print(sorted(cars,reverse=True))

print("Here is the original list again")
print(cars)

cars.reverse()
print(cars)

cars.reverse()
print(cars)

print(len(cars))

places = ['Norway','Iceland','Greenland','Morocco','Jordan']
print(places)

print(sorted(places))
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

len_places = len(places)

print(f"I am going to visit {len_places} places")

magicians = ['alice','david','carolina']

for magician in magicians:
	print(f"{magician.title()}, that was great trick")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone that was a great magic show")

pizzas = ['Margherita', 'Pepperoni','Farmhouse']

for pizza in pizzas:
	print(pizza)

for pizza in pizzas:
	print(f"I like {pizza} pizza")
print('I really like pizzas')

animals=['Dog','Cat','Hamster']

for animal in animals:
	print(animal)

for animal in animals:
	print(f"A {animal} would make a good pet")
print('Any of the above mentioned animals would make a great pet')

for i in range(7):
	print(i)
for i in range(1,6):
	print(i)

numbers=list(range(6))
print(numbers)

even_numbers=list(range(2,21,2))
print(even_numbers)

squares=[]

for value in range(1,11):
	square=value **2
	squares.append(square)
print(squares)

squares=[]

for value in range(1,11):
	squares.append(value**2)
print(squares)

squares=[value**2 for value in range(1,11)] #List comprehension
print(squares)

for i in range(1,21):
	print(i)

# for i in range(1,1000000):
# 	print(i)

mill_num=list(range(1,1000001))
print(min(mill_num))
print(max(mill_num))
print(sum(mill_num))

odd_numbers=list(range(1,20,2))
for odd_number in odd_numbers:
	print(odd_number)

three_multiples=list(range(3,31,3))
for three_multiple in three_multiples:
	print(three_multiple)

cubes = [value**3 for value in range(1,11)]
print(cubes)

players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team")

for player in players[:3]:
	print(player.title())

my_foods=['pizza','falafel','carrot cake']
friends_food=my_foods[:]

print(my_foods)
print(friends_food)

my_foods.append('cannoli')
friends_food.append('ice cream')

print(my_foods)
print(friends_food)