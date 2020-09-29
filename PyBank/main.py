import os
import csv
#designate the file path

banking_csv = os.path.join('','Resources','budget_data.csv')
#open csv file as read
with open(banking_csv,'r') as csvfile:
    csvs = csv.reader(csvfile, delimiter=',')
    #next cvs gets the header
    h = next(csvs)
    #creates all the initial variables and lists
    counter = 0
    changes = []
    sumProf = 0
    x = 0
    counter2 = 0
    incMax = 0
    decMin = 0
    #iterates through the rows in the cvs file
    for row in csvs:
        cast = int(row[1])
        #sums up all the profit into one variable
        sumProf = sumProf + cast
        y = x
        x = cast
        #calculates the change in profit month to month
        changesMonthly = x-y
        changes.append(changesMonthly)
        counter = counter + 1
        #calculates the worst and best months by comparing and holding the extreme values
        if decMin > incMax:
            counter2 = counter2 + 1
        if changesMonthly < decMin:
            worst = row[0]
            decMin = changesMonthly
        if changesMonthly > incMax:
            best = row[0]
            incMax = changesMonthly



    
    #prints out the analysis on the console of total months, total profit, and best and worst months
    print(f'Financial Analysis')
    print(f'---------------------------')
    print(f'Total Months: {counter}')
    print('Total: ${:.2f}'.format(sumProf))
    changes.pop(0)
    print('Average  Changes: ${:.2f}'.format(sum(changes)/len(changes)))
    print('Greatest Increase in Profits: {} (${:.2f})'.format((best), (incMax)))
    print('Greatest Decrease in Profits: {} (${:.2f})'.format((worst), (decMin)))
    print(f'---------------------------')

#creates the text file of the same printed out analysis, saves in analysis folder
ops = os.path.join('','analysis','analysis.txt')
with open(ops,"w") as bankFile:
    bankFile.write('Financial Analysis')
    bankFile.write('\n')
    bankFile.write(f'----------------------------')
    bankFile.write(f'Total Months: {counter}')
    bankFile.write('\n')
    bankFile.write('Total: ${:.2f}'.format(sumProf))
    bankFile.write('\n')
    bankFile.write('Average  Changes: ${:.2f}'.format(sum(changes)/len(changes)))
    bankFile.write('\n')
    bankFile.write('Greatest Increase in Profits: {} (${:.2f})'.format((best), (incMax)))
    bankFile.write('\n')
    bankFile.write('Greatest Decrease in Profits: {} (${:.2f})'.format((worst), (decMin)))
    bankFile.write('\n')
