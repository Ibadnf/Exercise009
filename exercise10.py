# buat class menghitung luas bangun:
# segitiga, persegi panjang, lingkaran
"""
class BangunSegitiga:

	def __init__(self, alas, tinggi, s1, s2, s3):
		self.alas = alas
		self.tinggi = tinggi
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3

	def kelilingSegitiga(self):
		print(self.s1 + self.s2 + self.s3)

	def luasSegitiga(self):
		print(self.alas * self.tinggi / 2)
		

myObjectx = BangunSegitiga(2, 3, 5, 5, 5)
myObjectx.kelilingSegitiga()
myObjectx.luasSegitiga()

class PersegiPanjang:

	def __init__(self, p, l, t):
		self.p = p
		self.l = l
		self.t = t

	def kelilingPersegi(self):
		print(self.p + self.l + self.p + self.l)

	def luasPersegi(self):
		print(self.p * self.l)

myObjecty = PersegiPanjang(5, 3, 4)
myObjecty.kelilingPersegi()
myObjecty.luasPersegi()
"""
#input name, jabatan

class PrintData(object):

	def __init__(self, nama, jabatan):
		self.nama = nama
		self.jabatan = jabatan

listData1 = PrintData("Luke", "Presiden")
listData2 = PrintData("Ibad", "Graphic Designer")
print(f"{listData1.nama}, {listData1.jabatan}")
print(f"{listData2.nama}, {listData2.jabatan}")


		