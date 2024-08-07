## INPUT GENERATOR

# for generating the file
import pandas as pd
# for tracking testcase number
import json
import os
# 
from person import Person


'''
    TO-DO:
      > randomize input
      > randomize number of exp counselors
      > randomize sex distribution
      > revise output result format
'''

class inputGenerator:

    boyNames =  [
        'Adam', 'Alex', 'Alejandro', 'Aaron', 'Austin', 'Aidan', 'Asher', 
                'Albert', 'Anthony', 
        'Brett', 'Buck', 'Ben', 'Blanton', 'Bando', 'Binh', 'Barry', 'Bruce',
        'Connor', 'Chase', 'Charlie', 'Carlos', 'Courtland', 'Clancy', 'Craig', 
                'Chris', 'Christopher',
        'Dylan', 'Dennis', 'Drew', 'Donald', 'David',
        'Eli', 'Ed', 
        'Fernan', 'Fred', 'Frank', 'Fez',
        'Grant', 'Gino', 'Guy',
        'Harry', 'Hank', 'Henry',
        'Ivan', 'Igor',
        'Jake', 'Jaden', 'Jacques', 'Jon', 'Jackson',
        'Kai', 'Klay', 'Klay', 'Kanye',
        'Louis', 'Logan',
        'Mark', 'Mike', 'Michael', 'Marshall',
        'Noah', 'Nick', 'Nate', 
        'Otto', 'Oscar', 'Oberon', 
        'Peter', 'Prince', 'Pablo', 'Phil', 'Philip', 'Preston',
        'Quentin', 'Quinn',
        'Ryan', 'Robert', 'Rich', 'Reed',
        'Sean', 'Sam', 'Seth', 'Steve', 'Simon', 
        'Tom', 'Travis', 'Toby', 'Tyler', 'Tory', 'Takeo', 'Trey', 'Trevor', 'Tony',
        'Ulysses', 
        'Victor', 
        'Will', 'Walter', 'Willard', 
        'Yuri', 
        'Zach', 'Zubiri', 
        ]
    girlNames = [
        'Angela', 'Ariella', 'Ashley', 'Audrey', 'Ariana', 'Andrea', 'Adriana',
        'Beth', 'Britney', 'Becca', 'Brazos',
        'Christine', 'Chloe', 'Charli', 'Caitlyn', 'Channary', 'Charlotte',
        'Danielle', 'Daphne', 'Delilah', 'Darcy',
        'Evelin', 'Emily', 'Eva', 'Elena',
        'Francesca', 'Fallon',
        'Georgia', 'Gabi', 'Grace', 'Gwen', 'Gina;,'
        'Hailey', 'Holly', 
        'Isabel', 'Ivy',
        'Jasmine', 'Jae', 'Jennifer', 'Jenna', 'Jordan',
        'Kim', 'Kylie', 'Kendall', 'Kristen', 'Kessa', 'Kate',
        'Lauren', 'Lucy', 'Laura', 'Lily', 'Love',
        'Mary', 'Meggie', 'Melissa', 'Mackenzie', 'Megan', 'Margot',
        'Natalie', 'Naomi', 'Nora',
        'Olivia', 
        'Peyton', 'Peri', 'Paige',
        'Quinley', 
        'Riley', 'Rachel', 'Rose', 'Reagan', 'Rebecca',
        'Skye', 'Serena', 'Savannah', 'Sara', 'Sue', 'Summer',
        'Tori', 'Tyla', 'Taylor',
        'Ursula', 'Violet', 'Victoria', 'Velma',
        'Winona', 
        'Xena', 'Ximena', 
        'Yvonne', 'Yvette', 'Yasmin',
        'Zoe', 'Zuri'
        ] 
    lastNames = [
        'Alcock', 'Allen', 'Amendola', 'Adams', 'Aniston'
        'Brand', 'Baxter', 'Bell', 'Baker', 'Bagheri', 'Black', 'Bravo', 'Banner',
                 'Barnett', 'Brinson', 'Burnett', 'Bellion', 'Battley', 
        'Chong', 'Crawford', 'Cochran', 'Cook', 'Coffee', 'Cloudsley', 'Cubert', 'Columbus',
        'Dean', 'Davidson', 'Dunn', 'Daniels', 'Day',
        'Elliot', 'Einspahr', 'Evans', 'Eilish',
        'Fox', 'Fallon', 'Freddo', 'FitzGibbon', 'Floreslovo', 'Fuches',
        'Garbarini', 'Gallager', 'Gunn', 'Goldberg', 'Garrido', 'Gray', 'Glover',
                'Gancarz', 'Guerra', 'Gangur', 'Geller',
        'Hope', 'Holt', 'Hemsworth', 'Hughes', 'Hermes', 'Hong', 'Harper', 
                'Hill', 'Hayes',
        'Ingram', 
        'James', 'Justice', 'Jordan',
        'Kafka', 'Kroll', 'Kammlah', 'Knight', 'Kelly', 'Kot', 'Krozel', 'Keene', 
                'Kerra', 'Kent',
        'LaFrance', 'Longoria', 'Li', 'Lehman', 'Lacey', 'Lanez',
        'Murdoch', 'McClane', 'Meer', 'Meyers', 'MacTavish', 'Maker',
        'Nop', 'North', 'Nguyen', 
        'Overfelt', 'Ortega', 'Ojeda', 'Oldman', 'Ochs', 'Odinson',
        'Parker', 'Petree', 'Peck', 'Priebe', 'Price', 'Pip',
        'Quincy', 'Quinn',
        'Russo', 'Reid', 'Richards', 'Rapp', 'Reynolds', 'Richtofen', 'Reyes',
                  'Rodriguez', 'Ramirez', 'Ripley', 'Rogers', 'Redd', 
        'Simpson', 'Stevens', 'Spears', 'Scott', 'Stone', 'Sung', 'Sun', 
                   'Struck', 'Stark', 'Summers',
        'Thompson', 'Tsui', 'Tays', 'Triola', 'Trusty',
        'Urquhart', 
        'Vicere', 'Vance', 'Vela',
        'Williams', 'White', 'Wray', 'Wong', 'Webster', 'Walters', 'Wright', 'Wiler', 'Wayne',
        'Young', 
        'Zane'
        ]
        

    # numThirdYears (<= 3) # includes 4th years
    # numSecondYears ( - numThirdYears <= 12)
        ## BEST METHOD IS PROBABLY:
        ##  start with assigning 12 first years, 6 male 6 female
        ##  add using randomizer between 1-2-3 and decrement from 2y/3y possible counts based on result
        ##  require at least 8 exp counselors

    def __init__(self, option:int=1, numExperienced:int=12): #, 
                #  numThirdYears:int=2, numSecondYears:int=10):
        self.option = option
        self.numExperienced = numExperienced
        # self.numThirdYears = numThirdYears
        # self.numSecondYears = numSecondYears
        # if(numExperienced != numThirdYears+numSecondYears):


    ## 
    ## 
    ## 
    ## 
    def generate(self):
        # TO-DO: RANDOMIZE INPUT 
        # What this is doing right now is giving pre-set 12 boy names (A-L) and 12 girl names (M-X)
        persons = []
        experienceLevel = 3
        count = 0
        for name in names:
            if (  (experienceLevel == 3 and len(persons) > 2)
               or (experienceLevel == 2 and len(persons > 12)) ):
                experienceLevel -= 1
            person = Person(name=name, exp=experienceLevel, 
                            sex=("M" if len(persons) <= 12 else "F"))
            persons.append(person)

        data = {
			'from':     [ name*24 for name in personNames ], # giver1*24, giver2*24, etc.
            'to':       personNames*24,      # 
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
        # return updated testcaseNum
        return testcaseNum