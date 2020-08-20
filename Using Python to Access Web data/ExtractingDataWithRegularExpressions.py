import re

file =  open("regex_sum_748911.txt", "r")
read = file.read()

num_list = re.findall('[0-9]+', read)
num_list = [int(i) for i in num_list]
summmation = sum(num_list)
print(summmation)
