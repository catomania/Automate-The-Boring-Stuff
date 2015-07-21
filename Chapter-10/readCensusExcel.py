#! python3
# read CensusExcel.py - tabulates population and number of census tracts for
# each county
# creates an allData list in a newly created Python file
# needs censuspopdata.xlsx Excel file to exist in current working directory

import openpyxl, pprint 
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx') #open the workbook
sheet = wb.get_sheet_by_name('Population by Census Tract') #grab the right sheet
countyData = {} #empty list to be filled

#todo: Fill in country data with each county's populatio and tracts.

print('Reading rows...')

for row in range(2, sheet.get_highest_row() + 1): #2 because you skip the column headers
    # Each row in the spreadsheet has data for 1 census tract.
    state = sheet['B' + str(row)].value #grab value for state
    county = sheet['C' + str(row)].value 
    pop     = sheet['D' + str(row)].value 

    #Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # make sure the key for the county in the state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    #each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    #increase the county pop by the pop in the census tract
    countyData[state][county]['pop'] += int(pop)

#open new text file and write the contents of countyData to it

print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')
