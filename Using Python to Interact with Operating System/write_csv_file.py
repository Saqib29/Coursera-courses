import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open("directory_name/write_csv.csv", "w") as hosts_csv:
    writer =  csv.writer(hosts_csv)
    writer.writerows(hosts) # writer.writerow for write one row, but writerows for multi line


with open("directory_name/write_csv.csv", "r") as file:
    lines = csv.reader(file)
    for line in lines:
        if len(line) < 2:
            continue
        host, ip = line
        print("Host: {}, IP: {}".format(host, ip))
