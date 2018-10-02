import math
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
	


		# print(gcd(20,10))

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


myf = Fraction(2,3)
frac1 = Fraction(1,2)
frac2 = Fraction(3,5)
total = frac1/frac2
print(total)
# print(myf)
