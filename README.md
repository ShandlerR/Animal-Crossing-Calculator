# Animal-Crossing-Calculator
A Class I wrote that will calculate how many bells will you profit when burying x bells as a money tree. Takes in 4 pieces of information: 

Minimum Bells: The Minimum amount that will be used when displaying results. If you wanted to see every profit chance ranging from 5,000 to 90,000, Minimum Bells would be that 5,000

MaxBells: The Maximum amount that will be used when displaying results. If you wanted to see every profit chance ranging from 5,000 to 90,000, Maximum Bells would be that 90,000

Step: The amount the program will step up for the next display. if we wanted to see the results for 0 ; 5,000 ; 10,000 ; 15,000 ; 20,000 The step would be 5,000 because we are incrementing 5,000 higher each input(set to 1 if a single output is required.)

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
