import sys

import csv

from os.path import exists

print(sys.argv)

input_path = sys.argv[1]

output_path = sys.argv[2]

if len(sys.argv) < 3:
    print("Not enough parameters")
    sys.exit

if not exists(sys.argv[1]):
    print("File not found")
    sys.exit()

if not exists(sys.argv[2]):
    print("File not found")
    sys.exit()

with open(input_path, 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
              
for parameter in sys.argv[3:]:
    parameter_list = parameter.split(',')
    new_value = ",".join(parameter_list[2:])
    print(parameter_list[0], parameter_list[1], new_value)


with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(sys.argv)

