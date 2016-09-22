#!/usr/bin/python
#By Etienne Noumen, @enoumen, http://enoumen.com
import sys,csv,operator,datetime

#File_Name=sys.argv[0]
File_Name="TSE_sample_data.csv"

# Open a file in read only mode
with open(File_Name, "rb") as infile, open("Output_File_Name.csv", "wb") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=False)
    header=reader.next()
    writer.writerow(header)    
    for i, line in enumerate(reader):
        #if i < 1:
        #   continue 
        start_date = line[13]
        print "Start Date:", start_date
        start_date_in_datetime_format=datetime.datetime.fromtimestamp(float(start_date))
        year=start_date_in_datetime_format.year
        month=start_date_in_datetime_format.month
        day=start_date_in_datetime_format.day
        hour=start_date_in_datetime_format.hour
        minute=start_date_in_datetime_format.minute
        if datetime.datetime(year, month, day, hour, minute) < datetime.datetime(2010, 9, 6, 0, 0):
           writer.writerow(line)


#Sorting word colum in ascending order by start_date
with open("Output_File_Name.csv", "rb") as infile, open("Sorted_Word_Column_File.csv", "wb") as csvfile:
    reader=csv.reader(infile)
    writer=csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["start_date"," Word"])
    header=reader.next()
    rest = [row for row in reader]
    sortedlist = sorted(rest, key=lambda row: float(row[13]), reverse=True)
    for row in sortedlist:
        start_date_sorted=row[13]
        start_date_sorted_in_datetime_format=datetime.datetime.fromtimestamp(float(row[13]))
        word_sorted=row[16]
        sorted_line=start_date_sorted + "," + word_sorted 
        writer.writerow([start_date_sorted,word_sorted])

 
