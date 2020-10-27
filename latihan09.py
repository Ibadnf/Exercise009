personAndPets = [
	{
		"name": "John Doe",
		"pets": [
			{"name": "Rooster"},
			{"name": "Dog"}
		]
	},

	{
		"name": "Luke Skywalker",
		"pets": [
			{"name": "Duck"},
			{"name": "Camel"}
		]
	},

	{
		"name": "Padme Amidala",
		"pets": [
			{"name": "Bird"},
			{"name": "Fish"}
		]
	}
]

for x in personAndPets:
	print(x)

class PersonAndAnimal:

	def function(self, person, animal):
		self.person = person
		self.animal = animal

	def getNama(self):
		for x in personAndPets:
			print(x["name"])

	def getAnimal(self):
		for i in personAndPets:
			print(i["pets"])

	def printAnimalbyPerson(self):
		for h in personAndPets:
			if h["name"] == "John Doe":
				for x in h["pets"]:
					print(x)
# belom terpecahkan:
	def cetakPersonbyAnimal(self):
		for o in personAndPets:
			for b in o["pets"]:
				if b == "Rooster":
					print(o["name"])


myObjectx = PersonAndAnimal()
myObjectx.getNama()
myObjectx.getAnimal()
myObjectx.printAnimalbyPerson()
myObjectx.cetakPersonbyAnimal()

for x in personAndPets:
	if x["name"] == "John Doe" or "Luke Skywalker" or "Padme Amidala":
		print("True")
	else:
		print("False")

for i in personAndPets:
	if i["name"] == "John Doe" or "Luke Skywalker" or "Padme Amidala":
		for v in i["pets"]:
			print("ini binatang")
	else:
		print("False")