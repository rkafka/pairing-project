class Person:
	def __init__(self, name:str, exp:int, prefList,
				 sex:str="x"):
		self.name = name
		self.exp = exp
		# to implement later
		self.prefList = None
		self.sex = sex

	def setAntiPref(self, antiprefs:List[Person]):
		return -1
