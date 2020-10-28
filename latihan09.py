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

class PersonPets:
    def __init__(self, person=None, pets=None):
        self.person = person
        self.pets = pets

    def getPetByPerson(self):
        for x in personAndPets:
            if x["name"] == self.person:
                print(x)

    def getPetAja(self):
        for x in personAndPets:
            if x["name"] == self.person:
                for p in x["pets"]:
                    print(p["name"])

    def getPersonByPet(self):
        for x in personAndPets:
            for p in x["pets"]:
                if p["name"] == self.pets:
                    print(x["name"])

    def cekMilik(self):
        for x in personAndPets:
            if (x["name"] == self.person):
                for p in x["pets"]:
                    if p["name"] == self.pets:
                        print("True")
                        fstartApp()
        print("False")

def fstartApp():
    print("\n==========")
    print("What to do? (Tulis Angka untuk Lanjut!)")
    print("1. Show all data on the list!")
    print("2. Show Pet by Person!")
    print("3. Show Person by Pet!")
    print("4. Cek Milik!\n")

    pilih = None
    pilih = input("")
    if(pilih == "1"):
        print("1. Show all data on the list!")
        #menampilkan list person dan pet
        print("\n#menampilkan list person dan pet")
        for x in personAndPets:
            print(x)
        fstartApp()

    elif(pilih == "2"):
        print("2. Show Pet by Person!")
        for listName in personAndPets:
            print(">> " + listName["name"])
        print("\n")
        namePerson = input("Type the name person: ")
        for listName in personAndPets:
            if (namePerson == listName["name"]):
                print("Pets owned by %s is: " % namePerson)
                petAja = PersonPets(person = namePerson)
                petAja.getPetAja()
                fstartApp()
            
        print("Liat yang bener! ULANGI LAGI")
        fstartApp()

    elif(pilih == "3"):
        print("3. Show Person by Pet!")
        for x in personAndPets:
            for namePets in x["pets"]:
                print(">> " + namePets["name"])

        print("\n")
        namePet = input("Type the name pet: ")
        for x in personAndPets:
            for namePets in x["pets"]:
                if (namePet == namePets["name"]):
                    print("Person who owned %s is: " % namePet)
                    getPerson = PersonPets(pets = namePet)
                    getPerson.getPersonByPet()
                    fstartApp()
                
        print("Liat yang bener! ULANGI LAGI")
        fstartApp()

    elif(pilih == "4"):
        print("4. Cek Milik!")
        namePerson = input("Type name person: ")
        namePets = input("Type name pet: ")
        cekMilik1 = PersonPets(person = namePerson, pets = namePets)
        cekMilik1.cekMilik()

    else:
        print("Baca yang bener!")

fstartApp()
		













"""KODE SAYA
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
"""