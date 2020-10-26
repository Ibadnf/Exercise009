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
	if x["name"] == "John Doe":
		for p in x["pets"]:
			print(p)


class personPets:

	def __init__(self, person=None, pets="Camel"):
		self.person = person
		self.pets = pets

	def getPetbyPerson(self):
		for x in personAndPets:
			if x["name"] == self.person:
				for p in x["pets"]:
					print(p)


pp = personPets(person="Luke Skywalker")
pp.getPetbyPerson()