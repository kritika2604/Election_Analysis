# Add our dependencies.
import csv
import os


# Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Resources/analysis","election_analysis.txt")

#Open   the election results and read the file. 
with open(file_to_load) as election_data:
    
# To do: read and analyze the data here.
    file_reader=csv.reader(election_data)

#print header row
    headers=next(file_reader)
    print(headers)
#for row in file_reader:
 # print(row)



# To write to files 

with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")
    txt_file.write("\nArapahoe \nDever\nJefferson")
   





# Data to be retrieved
# 1. Total number of votes cast
# 2. A complete list of candidates receiving votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of election based on popular votes


# Create a filename variable to a direct or indirect path to the file.




