import csv

file = open("directory_name/file.csv")
lines = csv.reader(file)
for line in lines:
    first_name, last_name, id = line
    print("Name: {:>8}, Full Name: {:>15}, ID: {:>6}".format(first_name, first_name+" "+last_name, id))

file.close()
