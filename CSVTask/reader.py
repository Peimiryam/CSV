import csv

with open("in.csv") as f_in, open("out.csv", 'w') as f_out:
    try:
    # Write header
        header = f_in.readline()
        f_out.write(header)

    except FileNotFoundError:
        print("Sorry. File not found.")

    #
    for line in f_in:
        f_out.write(line.lower())

r = csv.reader(open('out.csv'))
lines = list(r)

lines[3][0] = 'Planescape Torment'

writer = csv.writer(open('out.csv', 'w'))
writer.writerows(lines)

