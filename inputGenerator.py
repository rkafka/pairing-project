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
                'Albert', 'Anthony', 'Aubrey', 'Alvin', 'Alan', 
        'Brett', 'Buck', 'Ben', 'Blanton', 'Bando', 'Binh', 'Barry', 'Bruce', 
                'Brian', 'Bryan', 'Bernie', 'Babila', 'Beau', 'Blake',
        'Connor', 'Chase', 'Charlie', 'Carlos', 'Courtland', 'Clancy', 'Craig', 
                'Chris', 'Christopher', 'Cristoph', 'Chance', 'Cole', 'Clark', 
                'Cooper', 'Charles',
        'Dylan', 'Dennis', 'Drew', 'Donald', 'David', 'Desmond', 'Devin', 'Dom', 
                'Dominic', 'Damian', 
        'Eli', 'Ed', 'Evan', 'Everett', 'Elijiah', 'Elliot', 'Elias', 'Ezekiel',
        'Fernan', 'Fred', 'Frank', 'Fez', 'Francis', 'Filly', 'Forrest', 
        'Grant', 'Gino', 'Guy', 'Giancarlo', 'Gabriel', 'Gabe', 'Grayson', 
                'Giannis', 
        'Harry', 'Hank', 'Henry', 'Hughie', 'Hunter', 'Hudson', 'Hugh', 'Harrison', 
        'Ian', 'Isaac', 'Isaiah', 'Ivan', 'Igor', 'Irving', 'Iggy', 
        'Jake', 'Jaden', 'Jacques', 'Jon', 'Jackson', 'Jack', 'Joseph', 
        'Kai', 'Klay', 'Klay', 'Kanye', 'Kirk', 'Kevin', 'King', 'Keller', 
        'Louis', 'Logan', 'Lamar', 'Luka', 'Luke', 'Lucas', 'Leo', 'Levi', 
        'Mark', 'Mike', 'Michael', 'Marshall', 'Marvin', 'Marcel', 'Matteo', 
                'Maverick', 'Mason', 
        'Noah', 'Nick', 'Nate', 'Nigel', 'Nico', 'Nolan', 'Nash', 'Nikolai', 'Noble', 
        'Otto', 'Oscar', 'Oliver', 'Odie', 
        'Peter', 'Prince', 'Pablo', 'Phil', 'Philip', 'Preston', 'Patrick', 'Paul', 
                'Percy',
        'Quentin', 'Quinn', 'Quincy', 
        'Ryan', 'Robert', 'Rich', 'Reed', 'Reggie', 'Ryker',
        'Sean', 'Sam', 'Seth', 'Steve', 'Simon', 'Scott', 'Silas', 'Sebastian', 
                'Santiago', 'Sawyer', 
        'Tom', 'Travis', 'Toby', 'Tyler', 'Tory', 'Takeo', 'Trey', 'Trevor', 
                'Tony', 'Truman', 'Tyrell', 'Theo',
        'Ulysses', 'Uriah', 'Umar', 
        'Victor', 'Vinny', 'Vincent',
        'Will', 'Walter', 'Willard', 'Wyatt', 'Wesley', 'Wes', 
        'Xavier', 'Xander', 'Xion', 
        'Yuri', 'Yosef', 'Yahir', 
        'Zach', 'Zubiri', 'Zion', 'Zayn',
        ]
    girlNames = [
        'Angela', 'Ariella', 'Ashley', 'Audrey', 'Ariana', 'Andrea', 'Addison',
                'Adriana', 'Anna', 'Annie', 'Alice', 'Aurora', 
        'Beth', 'Britney', 'Becca', 'Brazos', 'Blayke', 'Billie', 'Bri', 'Briana', 
                'Brynn', 'Betty', 
        'Christine', 'Chloe', 'Charli', 'Caitlyn', 'Channary', 'Charlotte', 'Coi',
                'Camila', 'Clemintine', 'Cora', 'Caroline', 'Claire', 
        'Danielle', 'Daphne', 'Delilah', 'Darcy', 'Destiny', 'Diana', 'Dakota', 
        'Evelin', 'Emily', 'Eva', 'Elena', 'Ella', 'Emilia', 'Emma', 'Erin', 
                'Evelyn', 'Emerson', 
        'Francesca', 'Fallon', 'Felicity', 'Florence', 'Fiona', 'Farah', 'Faith', 
        'Georgia', 'Gabi', 'Grace', 'Gwen', 'Gina', 'Giovanna', 'Gigi', 'Glory', 
                'Gail', 
        'Hailey', 'Holly', 'Harper', 'Heidi', 
        'Isabel', 'Ivy', 'Irene', 'Ivanka', 'Izzy', 'Ingrid', 'Indiana', 'Imogene', 
        'Jasmine', 'Jae', 'Jennifer', 'Jenna', 'Jordan', 'Jillian', 'June', 'Janice', 
                'Joy', 'Jane', 'Judy', 'Juliana', 'Julia', 
        'Kim', 'Kylie', 'Kendall', 'Kristen', 'Kessa', 'Kate', 'Karen', 'Kelly', 
                'Katie', 'Kayla', 'Kourtney', 'Kathleen', 'Kat', 'Katherine', 
                'Kierra', 'Kiera',
        'Lauren', 'Lucy', 'Laura', 'Lily', 'Love', 'Lay', 'Lucille', 'Lacey', 
        'Mary', 'Meggie', 'Melissa', 'Mackenzie', 'Megan', 'Margot', 'Marissa', 
                'Maggie', 'Morgan', 'Mia', 'Molly', 'Maisie', 'Maeve', 'Mikayla', 
        'Natalie', 'Naomi', 'Nora', 'Nikita', 'Nellie', 'Niya', 'Nancy', 'Nadia', 
        'Olivia', 'Ophelia', 
        'Peyton', 'Peri', 'Paige', 'Phoenix', 'Piper', 'Penelope', 'Palmer', 
                'Pauline', 'Poppy', 
        'Quinley', 'Quinlan', 
        'Riley', 'Rachel', 'Rose', 'Reagan', 'Rebecca', 'Ren', 'Raven', 'Ruby', 
                'Ruth', 'Ryan', 'Rosalynn',
        'Sydney', 'Serena', 'Savannah', 'Sara', 'Sue', 'Summer', 'Siri', 'Sophie', 
                'Skye', 'Scarlet', 'Sloane', 'Sofia', 'Stella', 'Stephanie', 
        'Tori', 'Tyla', 'Taylor', 'Tara', 'Tina', 'Teagan', 'Tracy', 'Tyra', 'Talia', 
        'Ursula', 'Ulla', 'Udela', 
        'Violet', 'Victoria', 'Velma', 'Valerie', 'Val', 'Vivian', 'Viola', 'Vic', 
                'Veronica', 'Valentina', 
        'Winona', 'Wanda', 'Wilma', 'Whitney', 
        'Xena', 'Ximena', 
        'Yvonne', 'Yvette', 'Yasmin', 'Yara', 'Yelena', 
        'Zoe', 'Zuri', 'Zelda', 'Zara'
        ] 
    lastNames = [
        'Alcock', 'Allen', 'Amendola', 'Adams', 'Aniston', 'Ackles', 'Alonso', 'Ashmore', 'Ali',
        'Brand', 'Baxter', 'Bell', 'Baker', 'Bagheri', 'Black', 'Bravo', 'Banner',
                'Barnett', 'Brinson', 'Burnett', 'Bellion', 'Battley', 'Butcher',
                'Brown', 'Burns', 'Berkman', 'Benn', 'Bright', 'Burke',
        'Chong', 'Crawford', 'Cochran', 'Cook', 'Coffee', 'Cloudsley', 'Cubert', 
                'Columbus', 'Cage', 'Campbell', 'Capone', 'Curry', 'Cohen', 'Carrigan',
                'Cousineau', 'Carey', 'Carter', 'Carson', 'Cole',
        'Dean', 'Davidson', 'Dunn', 'Daniels', 'Day', 'Drake', 'Duckworth', 'Doncic',
        'Elliot', 'Einspahr', 'Evans', 'Eilish', 'Eslami', 'Esposito', 'East', 'Ether',
        'Fox', 'Fallon', 'Freddo', 'FitzGibbon', 'Floreslovo', 'Fuches', 'Fukuhara',
                'Fisher', 
        'Garbarini', 'Gallager', 'Gunn', 'Goldberg', 'Garrido', 'Gray', 'Glover',
                'Gancarz', 'Guerra', 'Gangur', 'Geller', 'Goggins', 'Greer', 'Graham', 
        'Hope', 'Holt', 'Hemsworth', 'Hughes', 'Hermes', 'Hong', 'Harper', 
                'Hill', 'Hayes', 'Hamill', 'Hamm', 'Hunter',
        'Ingram', 
        'James', 'Justice', 'Jordan', 'January', 'Jones', 'Jameson', 'Johnson', 
        'Kafka', 'Kroll', 'Kammlah', 'Knight', 'Kelly', 'Kot', 'Krozel', 'Keene', 
                'Kerra', 'Kent', 'Knowles', 'Keem', 'Kane',
        'LaFrance', 'Longoria', 'Li', 'Lehman', 'Lacey', 'Lanez', 'Lucado', 'Lamar', 
                'Lillard', 'Lane', 'Luck', 'Love', 
        'Murdoch', 'McClane', 'Meer', 'Meyers', 'MacTavish', 'Maker', 'Morgan', 
                'Miller', 'Mathers', 'Marquand', 'Moore', 'Malone', 'Milli', 'Marwa', 
                'Marchment', 'May',
        'Nop', 'North', 'Nguyen', 'Noir', 'Nowitski',
        'Overfelt', 'Ortega', 'Ojeda', 'Oldman', 'Ochs', 'Odinson', 'Odom',
        'Parker', 'Petree', 'Peck', 'Priebe', 'Price', 'Pazar', 'Pavelski', 
        'Quincy', 'Quinn', 'Quinto',
        'Russo', 'Reid', 'Richards', 'Rapp', 'Reynolds', 'Richtofen', 'Reyes', 'Raynor',
                'Rodriguez', 'Ramirez', 'Ripley', 'Rogers', 'Redd', 'Richter', 'Rogen', 
                'Rose', 'Riggs', 'Rigby',
        'Simpson', 'Stevens', 'Spears', 'Scott', 'Stone', 'Sung', 'Sun', 'Simmons', 
                   'Struck', 'Stark', 'Summers', 'Shaw', 'Sinclair', 'Smith',
        'Thompson', 'Tsui', 'Tays', 'Triola', 'Trusty', 'Toliver', 'Toews', 'Tiller',
        'Urquhart', 
        'Vicere', 'Vance', 'Vela',
        'Williams', 'White', 'Wray', 'Wong', 'Webster', 'Walters', 'Wright', 
                'Wiler', 'Wayne', 'Waltz', 'West', 'Winkler', 'Walker', 'Wells', 
        'Young', 'Yeun',
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