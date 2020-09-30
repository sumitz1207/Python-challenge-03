import csv
import os
#allows manipulation of date formats
from datetime import datetime
#dictionary of state -> state abbreviation
from us_state_abbrev import us_state_abbrev

#old file of employee data to update
old = os.path.join("employee_data.csv")

with open(old) as csvfile:
    #create new file for updated employee data
    update = os.path.join("updated_employee_data.csv")
    with open(update, 'w') as newF:
        #updated csv file needs first name and last name columns from split of name column
        writeUpdate = csv.DictWriter(newF, ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'States'])
        #write header
        writeUpdate.writeheader()
        #iterates through each row of the old file delimited by comma
        for i in csv.DictReader(csvfile, delimiter = ","):
            #splits first name and last name from the old file name column
            #converts YYYY-MM-DD to MM/DD/YYYY
            #converts first 7 digits of social to asterisks
            #coverts state name to state abbreviation
            writeUpdate.writerow({"Emp ID":i["Emp ID"], "First Name":str(i['Name']).split(" ")[0], "Last Name": str(i['Name']).split(" ")[1], "DOB": datetime.strptime(i["DOB"], "%Y-%m-%d").strftime("%m/%d/%Y"), "SSN": ("***-**-"+str(i['SSN']).split("-")[2]), "States": us_state_abbrev[i['State']]})