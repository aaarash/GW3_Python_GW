# import modules
import os
import csv

# filepath for data budget_data_2.csv
csvfilepath = os.path.join('Python_PyBank_RowData_budget_data_2_GW.csv')

with open(csvfilepath, newline='') as revenueData:
    csvreader = csv.reader(revenueData, delimiter=',')

    Month_Total = 0
    Revenue_Total = 0
    monthlyChange = 0
    
    GRT_Inc = 0
    GRT_Dec = 0
    
    firstRevenue = 0
    lastRevenue = 0
    Revenue_Total = 0

    revChange1 = []
    date1 = []
    table = {}

    GRT_IncDate = 0
    GRT_DecDate = 0

    firstRow = next(csvreader)  
    FirstRevenue_Row = next(csvreader) 
    firstRevenue = int(FirstRevenue_Row[1]) 
    

    for row in csvreader:
        
        Month_Total += + 1
        Revenue_Total += int(row[1])
        lastRevenue = int(row[1])
        
        date = str(row[0])
        date1.append(date)

        monthlyChange += lastRevenue - firstRevenue
        revChange = lastRevenue - firstRevenue

        revChange1.append(revChange)
        
        firstRevenue = lastRevenue
    
    Change_avg = monthlyChange / Month_Total
   
    Month_Total += + 1 
    Revenue_Total = Revenue_Total + int(FirstRevenue_Row[1])

    GRT_Dec = min(revChange1)
    GRT_Inc = max(revChange1)

    table = dict(zip(date1, revChange1))
    
    for date1, revChange1 in table.items():
        
        if (revChange1 == GRT_Inc):
            GRT_IncDate = date1

        elif (revChange1 == GRT_Dec):
            GRT_DecDate = date1          

print("Financial Analysis")
print("-------------------------------------------------------------")
print("\n")
print("Total Months: " + str(Month_Total))
print("Total Revenue: $" + str(Revenue_Total))
print("Average Revenue Change: $" + str(Change_avg))
print("Greatest Increase in Revenue: " + str(GRT_IncDate) + " ($" + str(GRT_Inc) + ")")
print("Greatest Decrease in Revenue: " + str(GRT_DecDate) + " ($" + str(GRT_Dec) + ")")

pyBankOutputPath = os.path.join('.', 'Python_PyBank_Output_GW.txt') 

with open(Python_PyBank_Output_GWPath, 'w', newline='') as textfile:
   
    textfile.writelines("Financial Analysis")
    textfile.writelines("-------------------------------------------------------------")
    print("\n")
    textfile.writelines("Total Months: " + str(Month_Total) + "\n")
    textfile.writelines("Total Revenue: $" + str(Revenue_Total) + "\n")
    textfile.writelines("Average Revenue Change: $" + str(Change_avg) + "\n")
    textfile.writelines("Greatest Increase in Revenue: " + "($" + str(GRT_Inc) + ")" + "\n")
    textfile.writelines("Greatest Decrease in Revenue: " + "($" + str(GRT_Dec) + ")" + "\n")