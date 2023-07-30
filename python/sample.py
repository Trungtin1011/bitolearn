# myarr = (1,2,3,4,5,6,7)

# print(myarr)
# print(myarr[0:2])
# print(myarr[1:])
# print(myarr[:3])

#######################################
### Read csv file simple way
#######################################
# import csv

# file_name = "employee.csv"

# with open(file_name, 'r', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


#######################################
### Read csv file detail way
#######################################
# # importing csv module
# import csv

# # csv file name
# filename = "university_records.csv"

# # initializing the titles and rows list
# fields = []
# rows = []

# # reading csv file
# with open(filename, 'r') as csvfile:
# 	# creating a csv reader object
# 	csvreader = csv.reader(csvfile)
	
# 	# extracting field names through first row
#     # .next() method returns the current row and advances the iterator to the next row
# 	fields = next(csvreader)

# 	# extracting each data row one by one
# 	for row in csvreader:
# 		rows.append(row)

# 	# get total number of rows
# 	print("Total no. of rows: %d"%(csvreader.line_num))

# # printing the field names
# print('Field names are:' + ', '.join(field for field in fields))

# # printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
# 	# parsing each column of a row
# 	for col in row:
# 		print("%10s"%col,end=" "),
# 	print('\n')


#######################################
### Write to csv file
#######################################

# # field names
# fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# # data rows of csv file
# rows = [ ['Nikhil', 'COE', '2', '9.0'],
#         ['Sanchit', 'COE', '2', '9.1'],
#         ['Aditya', 'IT', '2', '9.3'],
#         ['Sagar', 'SE', '1', '9.5'],
#         ['Prateek', 'MCE', '3', '7.8'],
#         ['Sahil', 'EP', '2', '9.1']]
 
# # name of csv file
# filename = "university_records.csv"
 
# # writing to csv file
# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
     
#     # writing the fields
#     csvwriter.writerow(fields)
     
#     # writing the data rows
#     csvwriter.writerows(rows)


print('1')
print('2')
print('3', end='')
print('4')