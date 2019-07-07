import csv
vote = []
candidate = []
khan = []
correy = []
li = []
otooley = []
total = 0.0
print('Election Results')
print('----------------------')
with open("election_Data.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter= ",")
    for row in csv_reader:
        vote.append(row[0])
        candidate.append(row[2])
    
    print('total vote: ' ,len(vote))    
    for row in (candidate):
        if row == "Khan":
            khan.append(row)
        perc =( len(khan) / len(vote)) * 100 
   
    print('Khan:' ,len(khan))
    print(perc, "%")
    
    for row in (candidate):
        if row == "Correy":
            correy.append(row)
        perc =( len(correy) / len(vote)) * 100 
    print('Correy:', len(correy))
    print(perc, "%")
    for row in (candidate):
        if row == "Li":
            li.append(row)
        perc2 =( len(li) / len(vote)) * 100 
    print('Li: ', len(li))
    print(perc2, "%")
    for row in (candidate):
        if row == "OTooley":
            
        
        
        
            otooley.append(row) 
        perc3 =( len(otooley) / len(vote)) * 100 
    print(perc3, "%")
        
    print("O'Tooley: ", len(otooley))
          

            
           