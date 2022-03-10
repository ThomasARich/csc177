import csv
from statistics import mean, median, stdev
from sklearn.decomposition import TruncatedSVD

out_rows = 5                                                        # Modify this value to change number of rows output.
row = 1
num_dup = 0
num_na = 0

candy_arr = [['']*7]*out_rows                                       # Declares array with 7 columns and out_rows # of rows.

id_list = []
med_list = []

candy_out = open('candy_out.csv','w', newline='')                   # Set candy_out.txt as output file.
with open('candyhierarchy2017.csv','r') as candy_in:                # Set candyhierarchy2017.csv as input file. NOTE: Use candyhierarchy2017_dup.csv to prove that duplicate entry deletion works.
    csv_in = csv.reader(candy_in)
    csv_out = csv.writer(candy_out)

    curr_row = next(csv_in)                                         # Writes the first 7 headers to the output file.
    for col in range(7):
        candy_arr[0][col] = curr_row[col]
    csv_out.writerow(candy_arr[0])

    while row < out_rows:
        # Preprocessing occurs here.
        curr_row = next(csv_in)

        if curr_row[0] in id_list:                                  # If there are any duplicate user IDs, the row is skipped and the number of duplicates is updated.
            num_dup += 1
        else:
            for col in range(7):
                if not curr_row[col]:
                    candy_arr[row][col] = 'N/A'
                    num_na += 1
                else:
                    candy_arr[row][col] = curr_row[col]
                    if col >= 6:
                        if curr_row[col] == 'DESPAIR':
                            med_list.append(0)
                        elif curr_row[col] == 'MEH':
                            med_list.append(1)
                        elif curr_row[col] == 'JOY':
                            med_list.append(2)                      # Outliers are deleted because anything that doesn't match the three supported values are ignored.
            csv_out.writerow(candy_arr[row])                        # Data written to output file.
            id_list.append(curr_row[0])
            row += 1

candy_out.close()                                                   # Close output file.
candy_in.close()                                                    # Close input file.

men = mean(med_list)
med = median(med_list)                                              # Calculate median value.
sdev = stdev(med_list)
svd = TruncatedSVD()
# svd.fit(candy_arr)
# transformed = svd.transform(candy_arr)
# print(candy_arr)

print("Number of duplicate entries removed: " + str(num_dup))
print("Number of missing values: " + str(num_na))
print('Numeric Mean opinion of 100 Grand Bars: ' + str(men))
print('Median opinion of 100 Grand Bars: ', end = '')
if med == 0:                                                        # NOTE: Hardcoded for 100 Grand Bar. Can be made dynamic if neccesary.
    print('0 (DESPAIR)')
elif med == 1:
    print('1 (MEH)')
elif med == 2:
    print('2 (JOY)')
else:
    print('UNDEFINED')
print('Numeric standard deviation of 100 Grand Bars opinion: ' + str(sdev))