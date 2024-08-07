class Person:
	def __init__(self, name:str, exp:int, sex:str=None):#, prefList:List=None):
		self.name = name
		self.exp = exp
		self.sex = sex
		# to implement later
		self.prefList = [None * 24]

	def __str__(self)->str:
		return self.name + " (" + str(self.exp) + "-year " + self.sex + ")"
		#return f"{self.name} ({self.exp}-year {self.sex})"

	def setAntiPref(self, antiprefs:List[Person]):
		return -1
