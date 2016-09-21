#run in python 3
import random as r
import pickle
import os
def main():

    #get powerball numbers and name values after setting favorite numbers
    pb, values= setFavoriteNumbers()
    
    #display names and powerball numbers
    for i in range(0,len(values)):
        
        print(values[i][0] + " " + values[i][1] + " " + str(pb[0]) + " " +
              str(pb[1]) + " " + str(pb[2]) + " " + str(pb[3]) + " " +
              str(pb[4]) + " Powerball: " + str(pb[5]))

    #display winning powerball numbers
    print("\n")
    print("Powerball winning number: \n")
    winningLotteryNumbers()
    
 

def setFavoriteNumbers():
    numbers = 'numbers.pkl'
    values = []

    #check if database exists and obtain values in database
    if os.path.exists(numbers):
        with open(numbers,'rb') as rfp:
            values = pickle.load(rfp)

    #enter data for all required components and do some error handling
    firstName = input("Enter your first name: ")
    while not firstName.isalpha():
        firstName = input("Not a valid name, Enter your first name: ")
    

    lastName = input("Enter your last name: ")
    while not lastName.isalpha():
        lastName = input("Not a valid name, Enter your last name: ")

        
    firstFav = input("select 1st # (1 thru 69): ")
    
    while  firstFav.isalpha() or int(firstFav) > 69 or int(firstFav) < 1:
        firstFav = input("Invalid input, select 1st # (1 thru 69): ")

    
    secondFav = input("select 2nd # (1 thru 69 excluding " + firstFav + "): ")
    while  secondFav.isalpha() or int(secondFav) > 69 or int(secondFav) < 1 or secondFav == firstFav:
        secondFav = input("Invalid input, select 2nd # (1 thru 69 excluding " + firstFav + "): ")


    thirdFav = input("select 3rd # (1 thru 69 excluding " + firstFav + " and " +
                  secondFav + "): ")
    while  thirdFav.isalpha() or int(thirdFav) > 69 or int(thirdFav) < 1 or thirdFav == firstFav or thirdFav == secondFav:
        thirdFav = input("Invalid input, select 3rd # (1 thru 69 excluding " + firstFav + " and " +
                  secondFav + "): ")

        
    fourthFav = input("select 4th # (1 thru 69 excluding " + firstFav +", " +
                 secondFav + ", and " + thirdFav + "): ")
    while  fourthFav.isalpha() or int(fourthFav) > 69 or int(fourthFav) < 1 or fourthFav == firstFav or fourthFav == secondFav or fourthFav == thirdFav:
        fourthFav = input("Invalid input, select 4th # (1 thru 69 excluding " + firstFav +", " +
                 secondFav + ", and " + thirdFav + "): ")
    

    fifthFav = input("select 5th # (1 thru 69 excluding " + firstFav +", " +
                 secondFav + ", " + thirdFav + ", and " + fourthFav + "): ")
    while  fifthFav.isalpha() or int(fifthFav) > 69 or int(fifthFav) < 1 or fifthFav == firstFav or fifthFav == secondFav or fifthFav == thirdFav or fifthFav == fourthFav:
        fifthFav = input("Invalid input, select 5th # (1 thru 69 excluding " + firstFav +", " +
                 secondFav + ", " + thirdFav + ", and " + fourthFav + "): ")

    
    sixthFav = input("select Power Ball # (1 thru 26): ")
    while  sixthFav.isalpha() or int(sixthFav) > 26 or int(sixthFav) <1:
        sixthFav = input("Invalid input, select Power Ball # (1 thru 26): ")


    #store data and append it to existing database
    print("\n\n")
    data = [firstName,lastName,firstFav,secondFav,thirdFav,fourthFav,fifthFav,sixthFav]
    values.append(data)
    with open(numbers,'wb') as wfp:
        pickle.dump(values,wfp)

    with open(numbers,'rb') as rfp:
        values = pickle.load(rfp)

    #check duplicate numbers and return value
    pb = getDuplicates(values)

    return pb,values
    

    
def getDuplicates(val):
    duplicates = 'duplicates.pkl'
    pb = 'powerballDups.pkl'

    #create array of data with all 69 potential numbers
    dups = [0] * 69
    powerballDups = [0] * 26
    pickle.dump(dups,open(duplicates,'wb'))
    pickle.dump(powerballDups,open(pb,'wb'))


    #load the data and process it
    for i in range(0,len(val)):
        for j in range(2,len(val[i]) - 1):
            number = val[i][j]
            with open(duplicates,'rb') as rfp:
               dups = pickle.load(rfp)
                        
            dups[int(number) - 1] += 1
            pickle.dump(dups,open(duplicates,'wb'))
    #load powerball data and process
    for ii in range(0,len(val)):
        powerballNumber = val[ii][7]
        powerballDups[int(powerballNumber) - 1] += 1
        pickle.dump(powerballDups,open(pb,'wb'))

    with open(duplicates,'rb') as rfp:
        dups = pickle.load(rfp)
    
    with open(pb,'rb') as rfp:
        powerballDups = pickle.load(rfp)

    #get the max counts for regular 5 numbers and powerball numbers
    pb = getMaxCountNumbers(dups,powerballDups)
    return pb
          
def getMaxCountNumbers(d,pbd):

    #set original maxes
    dmax = 0
    pbdmax = 0
    powerballNumbers = []
    for i in range(0,len(d)):
        if(d[i] >= dmax):
            dmax = d[i]

            #add on most favorable numbers
            powerballNumbers.append(i+1)
            
    for j in range(0,len(pbd)):
        
        if(pbd[j] > pbdmax):
            pbdmax = pbd[j]
            k = j
            
    #add on powerball number           
    powerballNumbers.append(k+1)
    
    return powerballNumbers              

#get winning lottery numbers            
def winningLotteryNumbers():
    numbers = []
    for i in range(5):
        number = r.randint(1,69)
        while (number in numbers):
            number = r.randint(1,69)
        numbers.append(number)
    numbers.sort()
    numbers.append(r.randint(1,26))
    print (str(numbers[0]) + " " + str(numbers[1]) + " " + str(numbers[2]) +
           " " + str(numbers[3]) + " " + str(numbers[4]) + " Powerball: "
           + str(numbers[5]))
    

main()
