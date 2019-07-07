import csv
month = []
mylist_total = []
total_amount = 0
average = []
avr = 0.0
total = 0.0
print('Financial Analysis')
print('-----------------------')
with open("budget_data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in reader:
        #new_month =row[0]
        month.append(row[0])
        # get the total in row 1
        mylist_total.append(int(row[1]))
    for row in range(1, len(mylist_total)):
        average.append(int(mylist_total[row] - int(mylist_total[row - 1])))
    # find the total month 
    print("Total Month : ", len(month))
    for i in mylist_total:
        total_amount += i
    print("total $:", total_amount)    
    
    averagerevenue = sum(average) / len(average)
    print('Average Change: ', averagerevenue)
    # to find the max 
    max_revenue = max(average)
    print('Greatest Increase in Profit: ', (month[average.index (max(average))]), (max_revenue))
    
    # to find the min
    min_revenue = min(average)
    print('Greatest Decrease in Profit: ',(month [average.index(min(average))]) , ( min_revenue))
    
      #  average.append(int(row[1]))
   
          
       # print(i)
      
          #  total_amount += x
        #total_amount = sum(row[1])
   # for x in average:
       # print(x)
      #  total += x
      #  print(total)
        #avr = x / total_amount
        #print(avr)
       # total += avr
        #print(total)
        # I should create a function that will calculate the total of  everything in the row and devide it by the total
       # avr = len(average) / total_amount
   # print('total month:', len(month))
   # print(mylist_total)
   # print('total:$',total_amount)
    #print(max(mylist_total))
   # print(avr)
        
        
                     
                     
       
    
        