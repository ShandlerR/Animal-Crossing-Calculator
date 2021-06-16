import random

class FindBells:

    def __init__(self, OverTenSuccessChance):
        """Organizes and runs the entire program."""
        self.get_Inputs()
        self.number_List = self.create_Number_List()
        self.success_Chance = OverTenSuccessChance
        self.output_Dicitonary = self.DoTheMath()
        self.show_Results()
    
    def get_Inputs(self):
        """Grabs All Inputs from the user.

        Args:
        MinBells: The Minimum amount that will be used when displaying results. If you wanted to see every profit chance ranging from 5,000 to 90,000, minBells would be that 5,000
        MaxBells: The Maximum amount that will be used when displaying results. If you wanted to see every profit chance ranging from 5,000 to 90,000, maxBells would be that 90,000
        Step: The amount the program will step up for the next display. if we wanted to see the results for 0 ; 5,000 ; 10,000 ; 15,000 ; 20,000 The step would be 5,000 because we are incrementing 5,000 higher each input(set to 1 if a single
        output is required.)
        Days: The Amount of time to test against. if we want to see how much money we could make in 10 days, buring 10,000 in the ground every day we would set days to 10. 

        Example: Show all results for 2,000 ; 4,000 ; 6,000 ; 8,000 if we bury every day for 10 days. 

        MinBells: 2000
        MaxBells: 8000
        Step: 2000
        Days: 10

        Example: Show ONLY 30,000 bells if we bury it every day for 100 days. 

        MinBells: 30000
        MaxBells: 30000
        Step: 1
        Days: 100
        """
        self.MinBells = int(input("What is the minimum bell Count you would to test against? \n"))
        self.MaxBells = int(input("What is the maximum bell Count you would to test against? \n"))
        self.Step = int(input('What would you like your step to be? \n'))
        self.Days = int(input('How many days will you like to be simulated? \n'))

    def create_Number_List(self):
        """Creates a list for all number between MinBells and Maxbells, with step included
        Args:
        MinBell: The minimum amount to be compared against
        MaxBells: The maximum amount to be compared against
        Step: the amount between each result"""
        NumberList = []
        for i in range(self.MinBells, self.MaxBells + self.Step, self.Step):
            NumberList.append(i)
        return NumberList

    def DoTheMath(self):
        """Takes the generated List of Numbers with the step included, and runs the simulation for the requested time. Returns a dictionary with the key being The Original input and the Value being The result after X days of simuation.
        also checks to see if we got back 3x bells, or 30,000 bells total. Subtracts The input each day.
        
        Args:
        Number_list: A list of all the required inputs, ranging from the minimum to the maximum with the step in between
        Days: The amount of days to be simulated
        myDictionary: A place to store the results in key value pairs"""
        ListOfNumbers = self.number_List
        DayCount = self.Days
        myDictionary = {}

        for BellCount in ListOfNumbers: #Grabs each input from List Of Numbers
            OverallBellCount = 0
            for _ in range(0, DayCount): #Runs the simulation for X days
                OverallBellCount -= BellCount #Removes the 'input' value each day (for reburial the next day)
                if BellCount <= 10000: #Compares to see if the input is over or under 10000 Bells
                    OverallBellCount += (BellCount * 2)
                else: #Else, rolls a random chance to see if 3x is returned, or 30,000
                    Chance = random.randint(1,100)
                    if Chance <= self.success_Chance:
                        OverallBellCount += (BellCount * 3)
                    else:
                        OverallBellCount += (10000 * 3)
            myDictionary[BellCount] = OverallBellCount #Stores all results in key(Input) value(money generated after sim.) Pairs.

        return myDictionary

    def show_Results(self):
        """Displays the output in format: 1,000(Input) | 10,000(Profit)
        
        Args:
        A dicitonary that has a key value pair, with the key being input and Value being the profit.
        """
        print("Input    |   Profit")
        print("-------------------")
        print("")
        for key in self.output_Dicitonary:
            print(f"{format(key, ',d')}   |   {format(self.output_Dicitonary[key], ',d')}")


FindBells(30)
""" The 30 Represents How likely you are to get over 10000 bells per bag. This Program Calcuates assuming that you will put back the same amount of bells that was originally planted (ie. if you plant 10,000 bells, and get 30,000 back, you
will replant 10,000 for day 2, making your profit for that day 20,000.)
"""