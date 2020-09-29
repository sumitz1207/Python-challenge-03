import os
import csv
#designate the file path
PyPoll_csv = os.path.join('', 'Resources', 'election_data.csv')
#creates all the initial variables and lists
ListOfCandidates = []
Total_voters = []
count = 0
All_votes = []
percentage_of_votes = []
candidate_percent = []
maximum_index = 0
rank = 0
#open cvs file as read
with open(PyPoll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #next of cvs gets the header
    header = next(csvreader)
    #create list of candidates with no duplicates and totals the votes
    for row in csvreader:
        Total_voters.append(row[0])
        candidate = row[2]
        if candidate in ListOfCandidates:
            candidate_index = ListOfCandidates.index(candidate)
            All_votes[candidate_index] = All_votes[candidate_index] +1
        else:
            ListOfCandidates.append(candidate)
            All_votes.append(1)
    #finds the winner by iterating through list and comparing each candidate, ranks them by percent of votes
    current_winner =All_votes[0]       
    for politician in range(len(ListOfCandidates)):
        rank = All_votes[politician]/len(Total_voters)
        percentage_of_votes = round(rank*100, 3)
        candidate_percent.append(percentage_of_votes)
        if All_votes[politician] > current_winner:
            current_winner = All_votes[politician]
            maximum_index = politician  
       
    #prints out the election results to the console/terminal
    print("Election Results")
    print("--------------------------")
    print(f'Total Votes: {len(Total_voters)}')    
    print("--------------------------")
    #interates through list of candidates to print out their percent and their total votes
    for politician in range(len(ListOfCandidates)):
        print(f'{ListOfCandidates[politician]}: {candidate_percent[politician]}% ({All_votes[politician]})')
    print("--------------------------")
    print(f'Winner:{ListOfCandidates[maximum_index]}')
    print("--------------------------")
   
#creates the text file of the same printed out analysis, saves in analysis folder
opf = os.path.join("", "analysis", "py_poll_analysis.txt")
with open(opf, "w") as electionFile:
    csv_write = csv.writer(electionFile)
    electionFile.write('Election Results')
    electionFile.write('\n')
    electionFile.write('------------------------')
    electionFile.write('\n')
    electionFile.write(f'Total Votes: {len(Total_voters)}')
    electionFile.write('\n')
    electionFile.write('------------------------')
    electionFile.write('\n')
    #iterates through list of candidates to print each other and their percent and total votes
    for pols in range(len(ListOfCandidates)):    
        electionFile.write(f' {ListOfCandidates[pols]}')
        electionFile.write(f': {candidate_percent[pols]}%')
        electionFile.write(f' ({All_votes[pols]})')
        electionFile.write('\n')
    electionFile.write('--------------------------')
    electionFile.write('\n')
    #announces winner
    electionFile.write(f'Winner: {ListOfCandidates[maximum_index]}') 
    electionFile.write('\n')
    electionFile.write('--------------------------')

           