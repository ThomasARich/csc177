candy_in = open("toomuchcandy500.txt","r")      # Set toomuchcandy500.txt as input file with read permissions
candy_out = open("candy_out.txt","w")            # Set candyout as output file.

try:                                            # Try-catch in case an error occurs in writing to outfile.
    for line in candy_in:                       # Reads every line in the infile and puts it in the outfile.
        candy_out.write(line)
except:
    print('File copy unsuccessful.')

print('File copy successful.')
candy_in.close()                                # Close input file.
candy_out.close()                               # Close output file.