import csv
from statistics import median

num_rows = 0
num_dup = 0
num_na = 0
curr_row = []
id_list = []
med_list = []

candy_out = open('candy_out.csv','w', newline='')                   # Set candy_out.txt as output file.
with open('candyhierarchy2017.csv','r') as candy_in:                # Set candyhierarchy2017.csv as input file. NOTE: Use candyhierarchy2017_dup.csv to prove that duplicate entry deletion works.
    csv_in = csv.reader(candy_in)
    csv_out = csv.writer(candy_out)

    row = next(csv_in)                                              # Writes the first 7 headers to the output file.
    for i in range(7):
        curr_row.append(row[i])
    csv_out.writerow(curr_row)

    while num_rows < 500:                                           # Replace value with number of lines desired in output file.
        curr_row.clear()
        # Preprocessing occurs here.
        row = next(csv_in)

        if row[0] in id_list:                                       # If there are any duplicate user IDs, the row is skipped and the number of duplicates is updated.
            num_dup += 1
        else:
            for i in range(7):
                if not row[i]:
                    curr_row.append('N/A')
                    num_na += 1
                else:
                    curr_row.append(row[i])
                    if i >= 6:
                        if row[i] == 'DESPAIR':
                            med_list.append(0)
                        elif row[i] == 'MEH':
                            med_list.append(1)
                        elif row[i] == 'JOY':
                            med_list.append(2)                      # Outliers are deleted because anything that doesn't match the three supported values are ignored.
            csv_out.writerow(curr_row)                              # Data written to output file.
            id_list.append(row[0])
            num_rows += 1

candy_out.close()                                                   # Close output file.
candy_in.close()                                                    # Close input file.

med = median(med_list)                                              # Calculate median value.

print("Number of duplicate entries removed: " + str(num_dup))
print("Number of missing values: " + str(num_na))
print('Median opinion of 100 Grand Bars: ', end = '')
if med == 0:                                                        # NOTE: Hardcoded for 100 Grand Bar. Can be made dynamic if neccesary.
    print('DESPAIR')
elif med == 1:
    print('MEH')
elif med == 2:
    print('JOY')
else:
    print('UNDEFINED')