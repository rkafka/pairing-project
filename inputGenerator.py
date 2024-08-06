## INPUT GENERATOR

# for generating the file
import pandas as pd
# for tracking testcase number
import json
import os
# 
from person import Person

class inputGenerator:

    # numThirdYears (<= 3) # includes 4th years
    # numSecondYears ( - numThirdYears <= 12)
        ## BEST METHOD IS PROBABLY:
        ##  start with assigning 12 first years, 6 male 6 female
        ##  add using randomizer between 1-2-3 and decrement from 2y/3y possible counts based on result
        ##  require at least 8 exp counselors

    def __init__(self, option:int=1):
		self.option = option

    ##
    ##
    ##
    def generate(self):
        names = ['Adam', 'Brett', 'Connor', 'Dylan', 'Evan', 'Fernan', 
                 'George', 'Harry', 'Ivan', 'Jake', 'Kyle', 'Louis',         # boys
                 'Mary', 'Naomi', 'Olivia', 'Peri', 'Quinley', 'Riley', 
                 'Savannah', 'Tori', 'Ursula', 'Violet', 'Winona', 'Yvonne'] # girls
        persons = []
        experienceLevel = 3
        count = 0
        for name in names:
            if (  (experienceLevel == 3 and len(persons) > 2) 
               or (experienceLevel == 2 and len(persons > 12)):
                experienceLevel -= 1
            person = Person(name=name, exp=experienceLevel, sex=("M" if len(persons) <= 12 else "F"), None)
            persons.append(person)

        data = {
			'from':     [ name*24 for name in personNames ] # giver1*24, giver2*24, etc.
            'to':       personNames*24      # 
            'ranking':  [ range(1,13,1) for _ in personNames ]
		}
		df = pd.DataFrame(data)
		df.to_csv('test')

	##
    ## Helper function used to determine the testcase 
    ## gives the '___' value in the input generated: 'test-input-___.csv'
    ##
	def getTestcaseNum(self, file_path='testcaseNum.json') -> int:
        # Load the current testcaseNum from the JSON file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                testcaseNum = data.get('testcaseNum', 0)
        else:
            testcaseNum = 0
    
        # Increment testcaseNum
        testcaseNum += 1
    
        # Save the updated testcaseNum to the JSON file
        with open(file_path, 'w') as file:
            json.dump({'testcaseNum': testcaseNum}, file)
    
        return testcaseNum