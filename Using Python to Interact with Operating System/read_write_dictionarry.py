import csv

users = [{"name": "sol Mansi", "username": "solm", "department": "IT Infrastructure"},
        {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
        {"name": "Charley Gray", "username": "greyc", "department": "Development"}]


keys = ["name", "username", "department"]

with open("directory_name/by_directory.csv", "w") as by_directory:
    writer = csv.DictWriter(by_directory, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


with open("directory_name/by_directory.csv") as file:
    lines = csv.DictReader(file)
    for line in lines:
        print(line)
