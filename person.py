class Person:
	def __init__(self, name:str, exp:int, sex:str="x", prefList:List=None):
		self.name = name
		self.exp = exp
		# to implement later
		self.prefList = None
		self.sex = sex

	def __str__(self)->str:
		return self.name + " (" + str(self.exp) + "-year " + self.sex + ")"
		#return f"{self.name} ({self.exp}-year {self.sex})"

	def setAntiPref(self, antiprefs:List[Person]):
		return -1
