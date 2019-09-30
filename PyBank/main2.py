# Avg, INC, and DEC are not calculating correctly

import os
import csv
csvpath = 'budget_data.csv'

# Define the function
def financial_analysis(csv_reader):
#define the variables
    change = 0
    changeList = []
    total_m= 0
    pnl_current = 0 
    total_pnl = 0
    changesum = 0
    avg_ch = 0
    pnl_previous = 0 
    inc = 0
    dec = 0
    idate = 0
    ddate = 0

    for row in csv_reader:
    #total months
        total_m += 1
    #set current profit and loss 
        pnl_current = (float(row[1]))
    #total profit and loss
        total_pnl += pnl_current
    #find change
        change = pnl_current - pnl_previous
    #add it to the list
        changeList.append(change)
    #find sum of your changes
        changesum = sum(changeList)
    #find average change
        avg_ch = changesum/total_m
    #find largest increase
        if pnl_current >= pnl_previous:
            inc = pnl_current
            idate= str(row[0])
    #find largest decrease
        if pnl_current <= pnl_previous:
            dec = pnl_current
            ddate = str(row[0])
    #pnl resent for each loop for sum        
            pnl_previous = pnl_current
        
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_m}")
    print(f"Total Profit and Loss: {total_pnl}")
    print(f"Average Change: {avg_ch}")
    print(f"Greatest Increase in Profit: {idate, inc}")
    print(f"Greatest Decrease in Profits: {ddate, dec}")

with open(csvpath, newline='') as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_reader)
    financial_analysis(budget_reader)



