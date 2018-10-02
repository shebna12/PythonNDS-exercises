def gcd(m,n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn

		print("n: ",n)
	return n 

class Fraction:
	def __str__(self):
		return str(self.num) + "/" + str(self.den)
	
	def __init__(self,top,bottom):
		self.num = top
		self.den = bottom
		if ((type(self.num) != int) or (type(self.den) != int)):
			raise Exception('This is the exception you expect to handle')
		if(self.den < 0):
			self.num = self.num * -1
			self.den = self.den * -1



	def __add__(self,otherfraction):
		newnum = self.num*otherfraction.den + self.den*otherfraction.num
		newden = self.den * otherfraction.den
		common = gcd(newnum,newden)
		print("newnum: ",newnum)
		print("newden: ",newden)
		return Fraction(newnum//common,newden//common)
		# return Fraction(newnum,newden)
	def __eq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def __sub__(self,otherfraction):
		newnum = self.num*otherfraction.den - self.den*otherfraction.num
		newden = self.den * otherfraction.den
		common = gcd(newnum,newden)
		print("newnum: ",newnum)
		print("newden: ",newden)
		return Fraction(newnum//common,newden//common)

	def __mul__(self,otherfraction):
		newnum = self.num*otherfraction.num
		newden = self.den*otherfraction.den
		common = gcd(newnum,newden)
		return Fraction(newnum//common,newden//common)

	def __truediv__(self,otherfraction):
		newnum = self.num*otherfraction.den
		newden = self.den*otherfraction.num
		common = gcd(newnum,newden)
		return Fraction(newnum//common,newden//common)

	def __gt__(self,otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num

		return newnum > newden

	def __ge__(self,otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num

		return newnum >= newden

	def __lt__(self,otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num

		return newnum < newden

	def __le__(self,otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num

		return newnum <= newden

	def __ne__(self,otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num

		return newnum != newden

	def __radd__(self,otherfraction):
		return otherfraction.__add__(self)

	def __iadd__(self,otherfraction):
		print("First ID: ",id(self.num))
		self.num = self.num*otherfraction.den + self.den*otherfraction.num
		self.den = self.den * otherfraction.den
		print("Second ID: ",id(self.num))
		common = gcd(self.num,self.den)
		print("newnum: ",self.num)
		print("newden: ",self.den)
		return Fraction(self.num//common,self.den//common)



myf = Fraction(2,3)
frac1 = Fraction(1,2)
frac2 = Fraction(2,4)
# print("frac1: ",frac1)
# print("frac2: ",frac2)

total = frac1.__iadd__(frac2)
print(total)
