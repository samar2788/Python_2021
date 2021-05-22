alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points=alien_0['points']
print(f"You have earned {new_points} points!!")

print(alien_0)

alien_0['x_position']=0
alien_0['y position']=25

print(alien_0)

alien_0={}

alien_0['color']='green'
alien_0['points']=5

print(alien_0)

alien_0={'color':'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color']='yellow'
print(f"The alien is now {alien_0['color']}")

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed']=='slow':
	x_increment=1
elif alien_0['speed']=='medium':
	x_increment=2
else:
	x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment
print(f"New position: {alien_0['x_position']}")

alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

favourite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

language=favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points','No point value assigned.')
print(point_value)

person={
	'first_name':'Samar',
	'last_name':'Bhargava',
	'age':32,
	'city':'Lucknow',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print(person.keys())

favourite_number={
	'Samar':27,
	'Parul':15,
	'Shashank':23,
	'Anu':29,
}
print(f"Samar's favourite number is {favourite_number['Samar']}")
print(f"Parul's favourite number is {favourite_number['Parul']}")
print(f"Shashank's favourite number is {favourite_number['Shashank']}")
print(f"Anu's favourite number is {favourite_number['Anu']}")

glossary = {
	'Samar':'A small island in the Phillipines',
	'Dick':'My penis',
	'Vagina':'Parul ki chut',
	'Ass':'Parul ki gaand',
}

print(f"Meaning of Samar is {glossary['Samar']}\n")
print(f"Meaning of Dick is {glossary['Dick']}\n")
print(f"Meaning of Vagina is {glossary['Vagina']}\n")
print(f"Meaning of Ass is {glossary['Ass']}\n")

user_0={
	'username':'efermi',
	'first':'enrico',
	'last':'fermi'
}

for key, value in user_0.items():
	print(f"\nKey:{key}")
	print(f"Value:{value}")

for name, language in favourite_languages.items():
	print(f"{name.title()}'s favourite labguage is {language.title()}")

for name in favourite_languages.keys():
	print(name.title())

friends = ['phil','sarah']

for name in favourite_languages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favourite_languages[name].title()
		print(f"\t{name.title()}, i see you love {language}")

for name in sorted(favourite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

favourite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

print("The following languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())

for language in set(favourite_languages.values()):
	print(language.title())

rivers={
	'nile':'egypt',
	'ganges':'india',
	'thames':'united kingdom',
}
for river in rivers.keys():
	print(f"The {river} runs through {rivers[river]}")

for river in rivers.keys():
	print(river)

for country in rivers.values():
	print(country)

alien_0={
	'color':'green',
	'points':5,
}
alien_1={
	'color':'yellow',
	'points':10,
}
alien_2={
	'color':'red',
	'points':15,
}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

aliens=[]

for alien_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color']='yellow'
		alien['speed']='medium'
		alien['points']=10
	elif alien['color']=='yellow':
		alien['color']='red'
		alien['speed']='fast'
		alien['points']=15

for alien in aliens[:5]:
	print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
	print(f"\t{topping}")

favourite_languages={
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}
for name , languages in favourite_languages.items():
	print(f"\n{name.title()}'s favourite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

users={
	'aeinstein':{
	'first':'albert',
	'last':'einstein',
	'location':'princeton',
	},
	'mcurie':{
	'first':'marie',
	'last':'curie',
	'location':'paris',
	},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name=f"{user_info['first']} {user_info['last']}"
	location=user_info['location']

	print(f"\tFull name : {full_name.title()}")
	print(f"\tLocation: {location.title()}")

	pet1 = {'animal':'dog','owner':'samar'}
	pet2 = {'animal':'cat','owner':'mohan'}
	pet3 = {'animal':'fish','owner':'jyoti'}

	pets = [pet1, pet2, pet3]

	for pet in pets:
		for a, o in pet.items():
			print(a, o)