import os
import datetime

# os.rename(old_name, new_name)
# os.remove(filename)
print('Exits: ',os.path.exists('areas.py'))       # os.path.extsts('file_name')
print('Size: ',os.path.getsize('areas.py'))      # os.path.getsize('file_name')

print('modified time: ',os.path.getmtime('areas.py'))      # os.path.getmtime('file_name')
# this time is called timestamp, it's actually UNIX timestyamp
# to modify it to make it readable datetime modul;e should use

timestamp = os.path.getmtime('areas.py')
date = datetime.datetime.fromtimestamp(timestamp)
print('Date: ',date)

# to know path whwre the file existed
path = os.path.abspath('areas.py')
print('Path: ',path)

# to see the current working directory
print("Current Directory: ",os.getcwd())

# to create new directory
os.mkdir('directory_name')

# to move new directory
os.chdir('directory_name')
print('Current Directory: ', os.getcwd())

# to remove directory we use, but it will work only when the directory is empty,
# otherwise we get an error
os.rmdir('directory_name')

#  os.listdir will give a list of all the files and sub-directories in that directory
lst = os.listdir('images')
