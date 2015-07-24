#! python3
# removeCsvHeader.py - removes header for all CSV files in cwd

import csv, os

#make file, but if exists, that's ok too
os.makedirs('headerRemoved', exist_ok=True)

#loop thru every file in cwd and find the csv files
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue #skip the non-csv files

    print('removing header from ' + csvFilename + '...')

    # read csv file (skipping first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num==1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    #write out csv file to the headerRemoved folder
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                      newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

print('Done!')
