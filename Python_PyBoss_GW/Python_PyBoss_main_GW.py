# Import modules 
import os
import csv

csvfilepath = os.path.join('Python_PyBoss_RowData_employee_data1_GW.csv')

with open(csvfilepath, newline='') as employeeData:
    csvreader = csv.DictReader(employeeData, delimiter=',')

    IDs = []
    DOBs = []
    SSNs = []
    States = []
    FirstNames = []
    LastNames = []
    
    State_Abb = {'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}    

    for row in csvreader: 
        IDs.append(row['Emp ID'])
        FirstNames.append(row['Name'].split(' ')[0])
        LastNames.append(row['Name'].split(' ')[1])
        DOBs.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        SSNs.append('***-**-' + row['SSN'].split('-')[2])
        States.append(State_Abb[row['State']])

    nEmployeeData = zip(IDs, FirstNames, LastNames, DOBs, SSNs, States)

pyBossOutputPath = os.path.join('.', 'Python_PyBoss_Output_GW.csv') 

with open(Python_PyBoss_Output_GWPath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    csvwriter.writerows(nEmployeeData)
   